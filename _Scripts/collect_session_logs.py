#!/usr/bin/env python
"""
collect_session_logs.py
AI session log collector for Claude / Copilot / Kiro.

Supports native macOS/Linux, WSL (reads Windows-side paths via /mnt/c/), and Windows.
Outputs collected conversations as structured Markdown to stdout or a file.

Usage:
    python _Scripts/collect_session_logs.py [options]

Options:
    --tool    all | claude | copilot | kiro     (default: all)
    --filter  all | latest | today | YYYY-MM-DD (default: all)
    --output  <path> | -                        (default: stdout)
"""

from __future__ import annotations

import argparse
import json
import os
import re
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


def _wsl_homes() -> list[Path]:
    """
    Find WSL user home directories from Windows via UNC paths.
    Tries \\\\wsl.localhost (Win11+) then \\\\wsl$ (older).
    Returns list of Paths like \\\\wsl.localhost\\Ubuntu\\home\\username.
    Only meaningful on sys.platform == 'win32'.
    """
    if sys.platform != "win32":
        return []

    distros: list[str] = []
    try:
        r = subprocess.run(
            ["wsl", "--list", "--quiet"],
            capture_output=True, timeout=10,
        )
        # wsl --list outputs UTF-16-LE on Windows
        text = r.stdout.decode("utf-16-le", errors="replace")
        distros = [
            d.strip().strip("\x00")
            for d in text.splitlines()
            if d.strip().strip("\x00")
        ]
    except Exception:
        pass

    homes: list[Path] = []
    for distro in distros:
        for prefix in (r"\\wsl.localhost", r"\\wsl$"):
            base = Path(f"{prefix}\\{distro}\\home")
            if not base.exists():
                continue
            try:
                candidates = sorted(
                    (d for d in base.iterdir() if d.is_dir()),
                    key=lambda d: d.stat().st_mtime,
                    reverse=True,
                )
                if candidates:
                    homes.append(candidates[0])
            except (PermissionError, OSError):
                pass
            break  # found a working prefix
    return homes


# ── Path discovery ───────────────────────────────────────────────────────────

def _claude_roots(win_home: Optional[Path], wsl_homes: list[Path] = []) -> list[Path]:
    roots = [
        Path(".claude"),
        Path.home() / ".claude",
        Path.home() / "Library" / "Application Support" / "Claude",
    ]
    if win_home:
        roots += [
            win_home / ".claude",
            win_home / "AppData" / "Roaming" / "Claude",
            win_home / "AppData" / "Local" / "Claude",
        ]
    for wsl_home in wsl_homes:
        roots += [
            wsl_home / ".claude",
        ]
    return [p for p in roots if p.exists()]


def _copilot_roots(win_home: Optional[Path], wsl_homes: list[Path] = []) -> list[Path]:
    roots = [
        Path.home() / ".config" / "github-copilot",
        Path.home() / "Library" / "Application Support" / "Code" / "logs",
        Path.home() / "Library" / "Application Support" / "Code - Insiders" / "logs",
    ]
    if win_home:
        roots += [
            win_home / "AppData" / "Roaming" / "GitHub Copilot",
            win_home / "AppData" / "Local" / "github-copilot",
            win_home / "AppData" / "Roaming" / "Code" / "logs",
            win_home / "AppData" / "Roaming" / "Code - Insiders" / "logs",
        ]
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "")
        if appdata:
            roots += [
                Path(appdata) / "Code" / "logs",
                Path(appdata) / "Code - Insiders" / "logs",
            ]
    return [p for p in roots if p.exists()]


def _kiro_roots(win_home: Optional[Path], wsl_homes: list[Path] = []) -> list[Path]:
    roots = [
        Path(".kiro") / "sessions" / "cli",
        Path.home() / ".kiro" / "sessions" / "cli",
        Path.home() / "Library" / "Application Support" / "Kiro",
    ]
    if win_home:
        roots += [
            win_home / ".kiro",
            win_home / "AppData" / "Roaming" / "kiro",
            win_home / "AppData" / "Local" / "kiro",
        ]
    for wsl_home in wsl_homes:
        roots += [
            wsl_home / ".kiro" / "sessions" / "cli",
            wsl_home / ".kiro",
        ]
    return [p for p in roots if p.exists()]


def _copilot_chat_roots(win_home: Optional[Path]) -> list[Path]:
    """Roots that contain workspaceStorage/*/chatSessions/*.json for Copilot Chat."""
    roots = [
        Path.home() / "Library" / "Application Support" / "Code" / "User" / "workspaceStorage",
        Path.home() / "Library" / "Application Support" / "Code - Insiders" / "User" / "workspaceStorage",
        Path.home() / ".config" / "Code" / "User" / "workspaceStorage",
    ]
    if win_home:
        roots += [
            win_home / "AppData" / "Roaming" / "Code" / "User" / "workspaceStorage",
            win_home / "AppData" / "Roaming" / "Code - Insiders" / "User" / "workspaceStorage",
        ]
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "")
        if appdata:
            roots += [
                Path(appdata) / "Code" / "User" / "workspaceStorage",
                Path(appdata) / "Code - Insiders" / "User" / "workspaceStorage",
            ]
    return [p for p in roots if p.exists()]


# ── Parsing helpers ──────────────────────────────────────────────────────────

# ── Copilot Chat session JSON helpers (ref: https://qiita.com/ysaki/items/8c0d8d2c03e49303c430) ──

def _ts_to_iso(ts_ms) -> Optional[str]:
    """Convert millisecond epoch timestamp to ISO 8601 string."""
    if ts_ms is None:
        return None
    try:
        return datetime.fromtimestamp(int(ts_ms) / 1000).isoformat()
    except (ValueError, TypeError):
        return None


def _cc_extract_agent_text(response: list) -> str:
    """Concatenate text blocks (kind=null) from a Copilot Chat response array."""
    return "".join(
        block.get("value", "")
        for block in response
        if isinstance(block, dict)
        and block.get("kind") is None
        and block.get("value")
    )


def _cc_extract_thinking(response: list) -> list[str]:
    """Extract thinking-process strings from a Copilot Chat response array."""
    return [
        block["value"]
        for block in response
        if isinstance(block, dict)
        and block.get("kind") == "thinking"
        and block.get("value")
    ]


def _cc_extract_tool_calls(response: list) -> list[dict]:
    """Extract tool invocation records from a Copilot Chat response array."""
    result = []
    for block in response:
        if not isinstance(block, dict) or block.get("kind") != "toolInvocationSerialized":
            continue
        inv = block.get("invocationMessage")
        past = block.get("pastTenseMessage")
        result.append({
            "toolId": block.get("toolId"),
            "toolCallId": block.get("toolCallId"),
            "isComplete": block.get("isComplete"),
            "invocationMessage": inv.get("value") if isinstance(inv, dict) else inv,
            "pastTenseMessage": past.get("value") if isinstance(past, dict) else past,
        })
    return result


def _cc_extract_file_edits(response: list) -> list[dict]:
    """Extract file edit records from a Copilot Chat response array."""
    return [
        {"uri": block.get("uri"), "done": block.get("done")}
        for block in response
        if isinstance(block, dict) and block.get("kind") == "textEditGroup"
    ]


def _parse_copilot_session_json(path: Path) -> Optional[dict]:
    """
    Parse a Copilot Chat session JSON file into a structured dict.
    Returns None if the file is not a valid Copilot Chat session.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return None

    if not isinstance(data, dict) or "requests" not in data:
        return None

    creation = data.get("creationDate")
    last_msg = data.get("lastMessageDate")
    duration: Optional[int] = None
    if creation and last_msg:
        try:
            duration = int((int(last_msg) - int(creation)) / 1000)
        except (ValueError, TypeError):
            pass

    session_meta = {
        "sessionId": data.get("sessionId"),
        "version": data.get("version"),
        "customTitle": data.get("customTitle"),
        "creationDate": _ts_to_iso(creation),
        "lastMessageDate": _ts_to_iso(last_msg),
        "durationSeconds": duration,
        "initialLocation": data.get("initialLocation"),
        "responderUsername": data.get("responderUsername"),
        "requesterUsername": data.get("requesterUsername"),
        "hasPendingEdits": data.get("hasPendingEdits"),
        "isImported": data.get("isImported"),
        "interactionsCount": len(data.get("requests") or []),
    }

    interactions: list[dict] = []
    for i, req in enumerate(data.get("requests") or []):
        if not isinstance(req, dict):
            continue

        ts = req.get("timestamp")
        model_state = req.get("modelState") or {}
        completed_at = model_state.get("completedAt") if isinstance(model_state, dict) else None
        dur_sec: Optional[int] = None
        if ts and completed_at:
            try:
                dur_sec = int((int(completed_at) - int(ts)) / 1000)
            except (ValueError, TypeError):
                pass

        agent = req.get("agent") or {}
        ext_id = agent.get("extensionId")
        response = req.get("response") or []
        msg = req.get("message") or {}
        var_data = req.get("variableData") or {}
        variables = var_data.get("variables") or []
        result = req.get("result") or {}

        interaction: dict = {
            "interactionIndex": i,
            "requestId": req.get("requestId"),
            "responseId": req.get("responseId"),
            "timestamp": _ts_to_iso(ts),
            "modelId": req.get("modelId"),
            "agent": {
                "name": agent.get("name"),
                "fullName": agent.get("fullName"),
                "extensionId": ext_id.get("value") if isinstance(ext_id, dict) else ext_id,
            },
            "modelState": {
                "value": model_state.get("value") if isinstance(model_state, dict) else None,
                "completedAt": _ts_to_iso(completed_at),
                "durationSeconds": dur_sec,
            },
            "timeSpentWaiting": req.get("timeSpentWaiting"),
            "userMessage": {
                "text": msg.get("text"),
                "partsCount": len(msg.get("parts") or []),
            },
            "variableData": {
                "variablesCount": len(variables),
                "variables": [
                    {
                        "name": v.get("name"),
                        "kind": v.get("kind"),
                        "isRoot": v.get("isRoot"),
                        "automaticallyAdded": v.get("automaticallyAdded"),
                    }
                    for v in variables
                    if isinstance(v, dict)
                ],
            },
            "agentResponse": {
                "text": _cc_extract_agent_text(response),
                "thinking": _cc_extract_thinking(response),
                "toolCalls": _cc_extract_tool_calls(response),
                "fileEdits": _cc_extract_file_edits(response),
                "responsePartsCount": len(response),
            },
            "result": {
                "details": result.get("details") if isinstance(result, dict) else None,
                "timings": result.get("timings") if isinstance(result, dict) else None,
            },
        }
        interactions.append(interaction)

    return {"session": session_meta, "interactions": interactions}


def _parse_copilot_transcript_jsonl(path: Path) -> Optional[dict]:
    """
    Parse a Copilot Chat transcript JSONL file.
    Format: workspaceStorage/{wsId}/GitHub.copilot-chat/transcripts/{sessionId}.jsonl
    Events: session.start / assistant.turn_start+end / assistant.message / tool.execution_*
    """
    try:
        raw_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None

    events: list[dict] = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    if not events:
        return None

    # セッションメタデータ抽出
    session_meta: dict = {}
    for ev in events:
        if ev.get("type") == "session.start":
            d = ev.get("data") or {}
            session_meta = {
                "sessionId": d.get("sessionId"),
                "startTime": d.get("startTime"),
                "producer": d.get("producer"),
                "copilotVersion": d.get("copilotVersion"),
                "vscodeVersion": d.get("vscodeVersion"),
            }
            break

    if not session_meta:
        return None

    # ツール実行結果インデックス（toolCallId → 結果）
    tool_exec: dict[str, dict] = {}
    for ev in events:
        t = ev.get("type")
        d = ev.get("data") or {}
        if t == "tool.execution_start":
            tid = d.get("toolCallId")
            if tid:
                tool_exec[tid] = {
                    "toolName": d.get("toolName"),
                    "arguments": d.get("arguments"),
                    "success": None,
                }
        elif t == "tool.execution_complete":
            tid = d.get("toolCallId")
            if tid and tid in tool_exec:
                tool_exec[tid]["success"] = d.get("success")

    # ターン単位でイベントをグループ化
    turns: list[dict] = []
    current: Optional[dict] = None

    for ev in events:
        t = ev.get("type")
        d = ev.get("data") or {}
        ts = ev.get("timestamp")

        if t == "assistant.turn_start":
            current = {
                "turnId": d.get("turnId"),
                "startTime": ts,
                "endTime": None,
                "messages": [],
                "reasoningTexts": [],
                "toolCalls": [],
            }
        elif t == "assistant.turn_end" and current is not None:
            current["endTime"] = ts
            turns.append(current)
            current = None
        elif t == "assistant.message" and current is not None:
            content = d.get("content") or ""
            reasoning = d.get("reasoningText")
            if content:
                current["messages"].append(content)
            if reasoning:
                current["reasoningTexts"].append(reasoning)
            for tr in (d.get("toolRequests") or []):
                if not isinstance(tr, dict):
                    continue
                tid = tr.get("toolCallId")
                ex = tool_exec.get(tid) or {} if tid else {}
                current["toolCalls"].append({
                    "toolCallId": tid,
                    "toolName": tr.get("name") or ex.get("toolName"),
                    "arguments": tr.get("arguments"),
                    "success": ex.get("success"),
                })

    if current is not None:  # 未閉模のターン
        turns.append(current)

    session_meta["turnsCount"] = len(turns)
    return {"session": session_meta, "turns": turns}


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
            message = obj.get("message") if isinstance(obj.get("message"), dict) else {}
            role = (
                message.get("role")
                or obj.get("role")
                or obj.get("type", "")
            )
            if role not in ("user", "assistant", "human"):
                continue
            text = _extract_text(
                message.get("content")
                or obj.get("content")
                or message.get("text")
                or obj.get("text")
                or ""
            )
            if text:
                messages.append({"role": role, "content": text})
    except OSError:
        pass
    return messages


def _parse_kiro_jsonl(path: Path) -> Optional[list[dict]]:
    """Parse a Kiro CLI .jsonl session file (Prompt / AssistantMessage format)."""
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
            kind = obj.get("kind")
            data = obj.get("data", {})
            if not isinstance(data, dict):
                continue
            if kind == "Prompt":
                role = "user"
            elif kind == "AssistantMessage":
                role = "assistant"
            else:
                continue
            parts = [
                block["data"]
                for block in data.get("content", [])
                if isinstance(block, dict)
                and block.get("kind") == "text"
                and isinstance(block.get("data"), str)
            ]
            text = "\n".join(p for p in parts if p)
            if text:
                messages.append({"role": role, "content": text})
    except OSError:
        pass
    return messages if messages else None


# ── Collection ───────────────────────────────────────────────────────────────

_MAX_MSG_CHARS = 4000   # truncate very long messages
_MAX_LOG_CHARS = 8000   # truncate raw log files


def _mtime(p: Path) -> datetime:
    return datetime.fromtimestamp(p.stat().st_mtime)

def _read_imported_paths(output_path: Path) -> set[str]:
    """Read already-imported source file paths from an existing output Markdown."""
    if not output_path.exists():
        return set()
    try:
        text = output_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()
    # Matches lines like: - path: `/some/path/to/log.jsonl`
    return set(re.findall(r"^- path: `([^`]+)`$", text, flags=re.MULTILINE))


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
    """Collect Copilot chat logs."""
    sessions: list[dict] = []
    for root in roots:
        for f in root.rglob("GitHub Copilot Chat.log"):
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
        for f in root.rglob("*.jsonl"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            msgs = _parse_kiro_jsonl(f)
            if msgs:
                sessions.append({
                    "tool": "kiro",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    "messages": msgs,
                })
    sessions.sort(key=lambda s: s["mtime"], reverse=True)
    return sessions[:1] if latest_only and sessions else sessions


def _collect_copilot_chat_sessions(
    roots: list[Path], since: Optional[date], latest_only: bool
) -> list[dict]:
    """Collect Copilot Chat structured session JSON files from workspaceStorage."""
    sessions: list[dict] = []
    for root in roots:
        # 新形式: workspaceStorage/{wsId}/GitHub.copilot-chat/transcripts/{sessionId}.jsonl
        for f in root.glob("*/GitHub.copilot-chat/transcripts/*.jsonl"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            parsed = _parse_copilot_transcript_jsonl(f)
            if parsed:
                sessions.append({
                    "tool": "copilot_chat",
                    "format": "transcript",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    **parsed,
                })
        # 旧形式: workspaceStorage/{wsId}/chatSessions/{sessionId}.json
        for f in root.glob("*/chatSessions/*.json"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            parsed = _parse_copilot_session_json(f)
            if parsed:
                sessions.append({
                    "tool": "copilot_chat",
                    "format": "chat_session",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    **parsed,
                })
        # 空ウィンドウ向け: globalStorage/emptyWindowChatSessions/{sessionId}.json
        for f in root.parent.glob("globalStorage/emptyWindowChatSessions/*.json"):
            mt = _mtime(f)
            if since and mt.date() < since:
                continue
            parsed = _parse_copilot_session_json(f)
            if parsed:
                sessions.append({
                    "tool": "copilot_chat",
                    "format": "chat_session",
                    "path": str(f),
                    "mtime": mt.isoformat(),
                    **parsed,
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


def _fmt_copilot_transcript(s: dict) -> str:
    """Format a parsed Copilot Chat transcript JSONL session as Markdown."""
    sess = s.get("session") or {}
    sid = sess.get("sessionId", "")
    lines = [
        f'### [COPILOT CHAT] {Path(s["path"]).stem}',
        f'- path: `{s["path"]}`',
        f'- mtime: `{s["mtime"]}`',
        f'- sessionId: `{sid}`',
        f'- startTime: `{sess.get("startTime", "")}`',
        f'- producer: `{sess.get("producer", "")}`',
        f'- copilotVersion: `{sess.get("copilotVersion", "")}`',
        f'- vscodeVersion: `{sess.get("vscodeVersion", "")}`',
        f'- turns: {sess.get("turnsCount", 0)}',
        "",
    ]
    for turn in s.get("turns") or []:
        turn_id = turn.get("turnId", "")
        start = turn.get("startTime", "")
        end = turn.get("endTime", "")
        lines.append(f'#### Turn {turn_id}  `{start}` → `{end}`')
        for i, msg in enumerate(turn.get("messages") or []):
            if len(msg) > _MAX_MSG_CHARS:
                msg = msg[:_MAX_MSG_CHARS] + "\n…（省略）"
            lines.append(f'**[assistant]**\n{msg}')
            lines.append("")
        if turn.get("reasoningTexts"):
            lines.append(f'**[reasoning]** {len(turn["reasoningTexts"])} block(s)')
            lines.append("")
        tool_calls = turn.get("toolCalls") or []
        if tool_calls:
            lines.append(f'**[tool calls]** {len(tool_calls)} call(s)')
            for tc in tool_calls:
                ok = "ok" if tc.get("success") else ("fail" if tc.get("success") is False else "?")
                lines.append(f'  - `{tc.get("toolName")}` [{ok}]')
            lines.append("")
    return "\n".join(lines)


def _fmt_copilot_chat_session(s: dict) -> str:
    """Format a parsed Copilot Chat session (old chatSessions JSON format) as Markdown."""
    sess = s.get("session") or {}
    title = sess.get("customTitle") or "(無題)"
    lines = [
        f'### [COPILOT CHAT] {title}',
        f'- path: `{s["path"]}`',
        f'- mtime: `{s["mtime"]}`',
        f'- sessionId: `{sess.get("sessionId", "")}`',
        f'- created: `{sess.get("creationDate", "")}`',
        f'- lastMessage: `{sess.get("lastMessageDate", "")}`',
        f'- durationSeconds: {sess.get("durationSeconds")}',
        f'- requester: `{sess.get("requesterUsername", "")}`',
        f'- interactions: {sess.get("interactionsCount", 0)}',
        "",
    ]
    for ia in s.get("interactions") or []:
        user_msg = ia.get("userMessage") or {}
        agent_resp = ia.get("agentResponse") or {}
        model_state = ia.get("modelState") or {}
        user_text = user_msg.get("text") or ""
        agent_text = agent_resp.get("text") or ""
        model = ia.get("modelId") or ""
        ts = ia.get("timestamp") or ""
        dur = model_state.get("durationSeconds")
        tool_calls = agent_resp.get("toolCalls") or []
        file_edits = agent_resp.get("fileEdits") or []
        thinking = agent_resp.get("thinking") or []

        if len(user_text) > _MAX_MSG_CHARS:
            user_text = user_text[:_MAX_MSG_CHARS] + "\n…（省略）"
        if len(agent_text) > _MAX_MSG_CHARS:
            agent_text = agent_text[:_MAX_MSG_CHARS] + "\n…（省略）"

        lines.append(f'#### Turn {ia["interactionIndex"] + 1}  `{ts}`  model: `{model}`  ({dur}s)')
        lines.append(f'**[user]**\n{user_text}')
        lines.append("")
        if thinking:
            lines.append(f'**[thinking]** {len(thinking)} block(s)')
            lines.append("")
        if tool_calls:
            lines.append(f'**[tool calls]** {len(tool_calls)} call(s)')
            for tc in tool_calls:
                lines.append(f'  - `{tc.get("toolId")}`: {tc.get("invocationMessage") or ""}')
            lines.append("")
        if file_edits:
            lines.append(f'**[file edits]** {len(file_edits)} file(s)')
            for fe in file_edits:
                lines.append(f'  - {fe.get("uri")}')
            lines.append("")
        lines.append(f'**[assistant]** (`{model}`)')
        lines.append(agent_text)
        lines.append("")
    return "\n".join(lines)


def _fmt_session(s: dict) -> str:
    if s["tool"] == "copilot_chat":
        if s.get("format") == "transcript":
            return _fmt_copilot_transcript(s)
        return _fmt_copilot_chat_session(s)
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

def _session_filename(s: dict) -> str:
    """
    Generate a filename stem for a session.
    Format: {agent}-{YYYY-MM-DD}-{short_id}  e.g. copilot-chat-2026-05-06-d3080de0
    Falls back to {agent}-{short_id} when date is unavailable.
    """
    tool = s["tool"]
    agent = tool.replace("_", "-")  # copilot_chat → copilot-chat

    start_iso: Optional[str] = None
    short_id: str = ""

    if tool == "copilot_chat":
        sess = s.get("session") or {}
        raw_date = sess.get("startTime") or sess.get("creationDate")
        if raw_date:
            start_iso = str(raw_date)[:10]  # "2026-05-06T..." → "2026-05-06"
        sid = sess.get("sessionId") or ""
        short_id = sid[:8] if sid else Path(s["path"]).stem[:8]
    elif tool == "copilot":
        # 生ログは親ディレクトリ名が全て同じため、パスのハッシュで一意化
        import hashlib
        start_iso = s["mtime"][:10]
        short_id = hashlib.md5(s["path"].encode()).hexdigest()[:8]
    else:
        start_iso = s["mtime"][:10]
        short_id = Path(s["path"]).stem[:8]

    if start_iso:
        return f"{agent}-{start_iso}-{short_id}"
    return f"{agent}-{short_id}"


def _is_dir_output(output: str) -> bool:
    """Return True if output should be treated as a directory (one file per session)."""
    if output == "-":
        return False
    p = Path(output)
    return p.is_dir() or output.endswith("/") or output.endswith(os.sep)

# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect AI session logs (Claude / Copilot / Kiro)"
    )
    parser.add_argument(
        "--tool",
        choices=["all", "claude", "copilot", "copilot_chat", "kiro"],
        default="all",
        help="Tool to collect (default: all)",
    )
    parser.add_argument(
        "--filter",
        default="all",
        help="Filter: all | latest | today | YYYY-MM-DD (default: all)",
    )
    parser.add_argument(
        "--output",
        default="-",
        help="Output: - for stdout | /path/to/dir/ for per-session files | /path/to/file for single file",
    )
    args = parser.parse_args()

    # ── Environment ──
    wsl = _is_wsl()
    win_native = sys.platform == "win32"
    win_home = _windows_home() if wsl else None
    wsl_homes = _wsl_homes() if win_native else []

    if wsl and win_home:
        env_desc = f"WSL  Windows home: {win_home}"
    elif wsl:
        env_desc = "WSL  Windows home: NOT FOUND"
    elif win_native:
        wsl_desc = ", ".join(str(h) for h in wsl_homes) if wsl_homes else "none found"
        env_desc = f"Windows  WSL homes: {wsl_desc}"
    elif sys.platform == "darwin":
        env_desc = "macOS / native"
    else:
        env_desc = "Linux / native"

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
        all_sessions += _collect_claude(_claude_roots(win_home, wsl_homes), since, latest_only)
    if args.tool in ("all", "copilot"):
        all_sessions += _collect_copilot(_copilot_roots(win_home, wsl_homes), since, latest_only)
    if args.tool in ("all", "copilot", "copilot_chat"):
        all_sessions += _collect_copilot_chat_sessions(
            _copilot_chat_roots(win_home), since, latest_only
        )
    if args.tool in ("all", "kiro"):
        all_sessions += _collect_kiro(_kiro_roots(win_home, wsl_homes), since, latest_only)

    all_sessions.sort(key=lambda s: s["mtime"], reverse=True)

    skipped_as_imported = 0
    is_dir = _is_dir_output(args.output)

    if not is_dir and args.output != "-":
        # 単一ファイルモード: 既出パスを読んで重複スキップ
        out = Path(args.output)
        imported_paths = _read_imported_paths(out)
        if imported_paths:
            before = len(all_sessions)
            all_sessions = [s for s in all_sessions if s["path"] not in imported_paths]
            skipped_as_imported = before - len(all_sessions)
    elif is_dir:
        # ディレクトリモード: 既存ファイル名で重複判定
        out_dir = Path(args.output)
        out_dir.mkdir(parents=True, exist_ok=True)
        existing = {p.stem for p in out_dir.glob("*.md")}
        before = len(all_sessions)
        all_sessions = [s for s in all_sessions if _session_filename(s) not in existing]
        skipped_as_imported = before - len(all_sessions)

    # ── Output ──
    generated = datetime.now().isoformat()

    if args.output == "-":
        # stdout: 全セッションを連結して出力
        header = [
            "# AI Session Log Collection",
            "",
            "| key | value |",
            "|---|---|",
            f"| generated | `{generated}` |",
            f"| tool | `{args.tool}` |",
            f"| filter | `{args.filter}` |",
            f"| environment | {env_desc} |",
            f"| sessions found | {len(all_sessions)} |",
            f"| skipped as imported | {skipped_as_imported} |",
            "",
            "---",
            "",
        ]
        if not all_sessions:
            header.append(
                "> No sessions found.  \n"
                "> Check that log files exist in the expected paths, or specify `--tool` and `--filter` explicitly."
            )
        else:
            for s in all_sessions:
                header.append(_fmt_session(s))
                header.append("\n---\n")
        print("\n".join(header))

    elif is_dir:
        # ディレクトリモード: セッションごとにファイルを生成
        written = 0
        for s in all_sessions:
            fname = _session_filename(s) + ".md"
            out_file = out_dir / fname
            file_content = "\n".join([
                f"# {_session_filename(s)}",
                "",
                "| key | value |",
                "|---|---|",
                f"| generated | `{generated}` |",
                f"| tool | `{s['tool']}` |",
                f"| source | `{s['path']}` |",
                "",
                "---",
                "",
                _fmt_session(s),
            ])
            out_file.write_text(file_content, encoding="utf-8")
            written += 1
        print(
            f"Wrote {written} session file(s) (skipped {skipped_as_imported} existing) → {out_dir}",
            file=sys.stderr,
        )

    else:
        # 単一ファイルモード
        out = Path(args.output)
        lines: list[str] = [
            "# AI Session Log Collection",
            "",
            "| key | value |",
            "|---|---|",
            f"| generated | `{generated}` |",
            f"| tool | `{args.tool}` |",
            f"| filter | `{args.filter}` |",
            f"| environment | {env_desc} |",
            f"| sessions found | {len(all_sessions)} |",
            f"| skipped as imported | {skipped_as_imported} |",
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
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists() and out.stat().st_size > 0:
            if all_sessions:
                out.write_text(out.read_text(encoding="utf-8", errors="replace") + "\n\n" + content, encoding="utf-8")
            print(
                f"Appended {len(all_sessions)} new session(s) (skipped {skipped_as_imported} imported) → {out}",
                file=sys.stderr,
            )
        else:
            out.write_text(content, encoding="utf-8")
            print(f"Wrote {len(all_sessions)} session(s) → {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
