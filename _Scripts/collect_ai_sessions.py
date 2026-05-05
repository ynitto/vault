#!/usr/bin/env python3
"""
collect_ai_sessions.py
AI session log collector for Claude / Copilot / Kiro.

Supports native Linux, WSL (reads Windows-side paths via /mnt/c/), and Windows.
Outputs collected conversations as structured Markdown to stdout or a file.

Usage:
    python _Scripts/collect_ai_sessions.py [options]

Options:
    --tool    all | claude | copilot | kiro   (default: all)
    --filter  latest | today | YYYY-MM-DD     (default: latest)
    --output  <path> | -                      (default: stdout)
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional


# ── Environment detection ────────────────────────────────────────────────────

def _is_wsl() -> bool:
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except OSError:
        return False


def _windows_home() -> Optional[Path]:
    """
    Resolve the Windows user home directory.
    Tries, in order:
      1. USERPROFILE env var (set by some WSL configs)
      2. cmd.exe %USERPROFILE%
      3. Scan /mnt/c/Users/ for an active user directory
    Returns a Path or None.
    """
    def _win_to_wsl(win_path: str) -> Optional[Path]:
        """Convert C:\\Users\\foo  →  /mnt/c/Users/foo"""
        p = win_path.strip().replace("\\", "/")
        for drive in "CDEFGHIJ":
            p = p.replace(f"{drive}:/", f"/mnt/{drive.lower()}/")
            p = p.replace(f"{drive.lower()}:/", f"/mnt/{drive.lower()}/")
        result = Path(p)
        return result if result.exists() else None

    # 1. Env var
    userprofile = os.environ.get("USERPROFILE", "")
    if userprofile:
        p = _win_to_wsl(userprofile)
        if p:
            return p

    # 2. cmd.exe
    try:
        r = subprocess.run(
            ["cmd.exe", "/c", "echo %USERPROFILE%"],
            capture_output=True, text=True, timeout=5,
        )
        p = _win_to_wsl(r.stdout)
        if p:
            return p
    except Exception:
        pass

    # 3. Scan /mnt/c/Users/
    SYSTEM_DIRS = {"Public", "Default", "Default User", "All Users"}
    users = Path("/mnt/c/Users")
    if users.exists():
        candidates = sorted(
            (d for d in users.iterdir() if d.is_dir() and d.name not in SYSTEM_DIRS),
            key=lambda d: d.stat().st_mtime,
            reverse=True,
        )
        for c in candidates:
            if (c / "AppData").exists():
                return c

    return None


# ── Path discovery ───────────────────────────────────────────────────────────

def _claude_roots(win_home: Optional[Path]) -> list[Path]:
    roots = [
        Path(".claude"),
        Path.home() / ".claude",
    ]
    if win_home:
        roots += [
            win_home / ".claude",
            win_home / "AppData" / "Roaming" / "Claude",
            win_home / "AppData" / "Local" / "Claude",
        ]
    return [p for p in roots if p.exists()]


def _copilot_roots(win_home: Optional[Path]) -> list[Path]:
    roots = [
        Path.home() / ".config" / "github-copilot",
    ]
    if win_home:
        roots += [
            win_home / "AppData" / "Roaming" / "GitHub Copilot",
            win_home / "AppData" / "Local" / "github-copilot",
            # VSCode chat logs (Insiders + stable)
            win_home / "AppData" / "Roaming" / "Code" / "logs",
            win_home / "AppData" / "Roaming" / "Code - Insiders" / "logs",
        ]
    return [p for p in roots if p.exists()]


def _kiro_roots(win_home: Optional[Path]) -> list[Path]:
    roots = [
        Path(".kiro"),
        Path.home() / ".kiro",
    ]
    if win_home:
        roots += [
            win_home / ".kiro",
            win_home / "AppData" / "Roaming" / "kiro",
            win_home / "AppData" / "Local" / "kiro",
        ]
    return [p for p in roots if p.exists()]


# ── Parsing helpers ──────────────────────────────────────────────────────────

def _extract_text(content) -> str:
    """Flatten Claude-style content blocks to plain text."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(block.get("text", ""))
                # skip tool_use / tool_result blocks
            elif isinstance(block, str):
                parts.append(block)
        return "\n".join(p for p in parts if p)
    return str(content) if content else ""


def _parse_claude_jsonl(path: Path) -> list[dict]:
    """Parse a Claude CLI .jsonl session file into message dicts."""
    messages: list[dict] = []
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            role = obj.get("role") or obj.get("type", "")
            if role not in ("user", "assistant", "human"):
                continue
            text = _extract_text(obj.get("content") or obj.get("text") or "")
            if text:
                messages.append({"role": role, "content": text})
    except OSError:
        pass
    return messages


def _parse_kiro_json(path: Path) -> Optional[list[dict]]:
    """Parse a Kiro /chat save JSON file. Returns messages or None."""
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return None

    # Accept only files that look like Kiro session data
    has_msgs = "messages" in data or "conversation" in data
    has_id = "conversation_id" in data or "session_id" in data.get("metadata", {})
    if not (has_msgs or has_id):
        return None

    raw_msgs = data.get("messages") or data.get("conversation") or []
    messages: list[dict] = []
    for m in raw_msgs:
        if not isinstance(m, dict):
            continue
        role = m.get("role") or m.get("type") or "unknown"
        text = _extract_text(m.get("content") or m.get("text") or "")
        if text:
            messages.append({"role": role, "content": text})
    return messages if messages else None


# ── Collection ───────────────────────────────────────────────────────────────

_MAX_MSG_CHARS = 4000   # truncate very long messages
_MAX_LOG_CHARS = 8000   # truncate raw log files


def _mtime(p: Path) -> datetime:
    return datetime.fromtimestamp(p.stat().st_mtime)


def _collect_claude(roots: list[Path], since: Optional[date], latest_only: bool) -> list[dict]:
    sessions: list[dict] = []
    for root in roots:
        for f in root.rglob("*.jsonl"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            msgs = _parse_claude_jsonl(f)
            if msgs:
                sessions.append({
                    "tool": "claude",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    "messages": msgs,
                })
    sessions.sort(key=lambda s: s["mtime"], reverse=True)
    return sessions[:1] if latest_only and sessions else sessions


def _collect_copilot(roots: list[Path], since: Optional[date], latest_only: bool) -> list[dict]:
    """Collect Copilot plain-text .log files."""
    sessions: list[dict] = []
    for root in roots:
        for f in root.rglob("*.log"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="replace").strip()
            except OSError:
                continue
            if text:
                sessions.append({
                    "tool": "copilot",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    "raw": text,
                })
    sessions.sort(key=lambda s: s["mtime"], reverse=True)
    return sessions[:1] if latest_only and sessions else sessions


def _collect_kiro(roots: list[Path], since: Optional[date], latest_only: bool) -> list[dict]:
    sessions: list[dict] = []
    for root in roots:
        for f in root.rglob("*.json"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            msgs = _parse_kiro_json(f)
            if msgs is not None:
                sessions.append({
                    "tool": "kiro",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    "messages": msgs,
                })
    sessions.sort(key=lambda s: s["mtime"], reverse=True)
    return sessions[:1] if latest_only and sessions else sessions


# ── Formatting ───────────────────────────────────────────────────────────────

def _fmt_messages(messages: list[dict]) -> str:
    lines: list[str] = []
    for msg in messages:
        role = msg["role"]
        text = msg["content"]
        if len(text) > _MAX_MSG_CHARS:
            text = text[:_MAX_MSG_CHARS] + "\n…（省略）"
        lines.append(f"**[{role}]**\n{text}")
        lines.append("")
    return "\n".join(lines)


def _fmt_session(s: dict) -> str:
    lines = [
        f'### [{s["tool"].upper()}] {Path(s["path"]).name}',
        f'- path: `{s["path"]}`',
        f'- mtime: `{s["mtime"]}`',
        "",
    ]
    if s["tool"] in ("claude", "kiro"):
        msgs = s.get("messages", [])
        lines.append(f'- turns: {len(msgs)}')
        lines.append("")
        lines.append(_fmt_messages(msgs))
    elif s["tool"] == "copilot":
        raw = s.get("raw", "")
        if len(raw) > _MAX_LOG_CHARS:
            raw = raw[:_MAX_LOG_CHARS] + "\n…（省略）"
        lines.append("```log")
        lines.append(raw)
        lines.append("```")
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect AI session logs (Claude / Copilot / Kiro)"
    )
    parser.add_argument(
        "--tool",
        choices=["all", "claude", "copilot", "kiro"],
        default="all",
        help="Tool to collect (default: all)",
    )
    parser.add_argument(
        "--filter",
        default="latest",
        help="Filter: latest | today | YYYY-MM-DD (default: latest)",
    )
    parser.add_argument(
        "--output",
        default="-",
        help="Output path or - for stdout (default: stdout)",
    )
    args = parser.parse_args()

    # ── Environment ──
    wsl = _is_wsl()
    win_home = _windows_home() if wsl else None
    env_desc = (
        f"WSL  Windows home: {win_home}" if wsl and win_home
        else "WSL  Windows home: NOT FOUND" if wsl
        else "Linux / native"
    )

    # ── Date filter ──
    since: Optional[date] = None
    latest_only = args.filter == "latest"
    if args.filter == "today":
        since = date.today()
    elif args.filter not in ("latest", "all"):
        try:
            since = datetime.strptime(args.filter, "%Y-%m-%d").date()
        except ValueError:
            pass

    # ── Collect ──
    all_sessions: list[dict] = []
    if args.tool in ("all", "claude"):
        all_sessions += _collect_claude(_claude_roots(win_home), since, latest_only)
    if args.tool in ("all", "copilot"):
        all_sessions += _collect_copilot(_copilot_roots(win_home), since, latest_only)
    if args.tool in ("all", "kiro"):
        all_sessions += _collect_kiro(_kiro_roots(win_home), since, latest_only)

    all_sessions.sort(key=lambda s: s["mtime"], reverse=True)

    # ── Build output ──
    lines: list[str] = [
        "# AI Session Log Collection",
        "",
        "| key | value |",
        "|---|---|",
        f"| generated | `{datetime.now().isoformat()}` |",
        f"| tool | `{args.tool}` |",
        f"| filter | `{args.filter}` |",
        f"| environment | {env_desc} |",
        f"| sessions found | {len(all_sessions)} |",
        "",
        "---",
        "",
    ]

    if not all_sessions:
        lines.append(
            "> No sessions found.  \n"
            "> Check that log files exist in the expected paths, or specify `--tool` and `--filter` explicitly."
        )
    else:
        for s in all_sessions:
            lines.append(_fmt_session(s))
            lines.append("\n---\n")

    content = "\n".join(lines)

    if args.output == "-":
        print(content)
    else:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"Wrote {len(all_sessions)} session(s) → {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
