<#
.SYNOPSIS
    Power Automate Desktop を起動し、Ctrl+Shift+R を送信する。

.DESCRIPTION
    PAD が未起動の場合は自動起動し、指定秒数待機後に Ctrl+Shift+R を送信します。
    PAD の実行ファイルが見つからない場合は Microsoft Store URI で起動を試みます。

.PARAMETER Wait
    PAD 起動後、キー送信までの待機秒数（デフォルト: 3）

.EXAMPLE
    .\launch_pad_shortcut.ps1
    .\launch_pad_shortcut.ps1 -Wait 5
#>

param(
    [double]$Wait = 3.0
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ---- PAD の実行ファイル候補 ----
$PadCandidates = @(
    "C:\Program Files (x86)\Power Automate Desktop\PAD.Console.Host.exe",
    "C:\Program Files\Power Automate Desktop\PAD.Console.Host.exe"
)

$PadStoreUri = "ms-powerautomate:"

# ---- PAD の実行ファイルを検索 ----
function Find-PadExe {
    foreach ($path in $PadCandidates) {
        if (Test-Path $path) {
            return $path
        }
    }
    return $null
}

# ---- PAD が実行中か確認 ----
function Test-PadRunning {
    $procs = Get-Process -Name "PAD*" -ErrorAction SilentlyContinue
    return ($null -ne $procs -and $procs.Count -gt 0)
}

# ---- PAD を起動 ----
function Start-Pad {
    param([string]$ExePath)

    if ($ExePath) {
        Start-Process -FilePath $ExePath
        Write-Host "[INFO] PAD を起動しました: $ExePath"
    } else {
        Start-Process $PadStoreUri
        Write-Host "[INFO] PAD を Store URI で起動しました: $PadStoreUri"
    }
}

# ---- PAD ウィンドウをフォアグラウンドに持ってくる ----
function Set-PadWindowFocus {
    Add-Type @"
using System;
using System.Runtime.InteropServices;
public class WinApi {
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
}
"@

    $procs = Get-Process -Name "PAD*" -ErrorAction SilentlyContinue
    if ($null -eq $procs -or $procs.Count -eq 0) {
        Write-Warning "[WARN] PAD プロセスが見つかりませんでした。アクティブなウィンドウに送信します。"
        return
    }

    $hwnd = $procs[0].MainWindowHandle
    if ($hwnd -ne [IntPtr]::Zero) {
        # SW_RESTORE = 9
        [WinApi]::ShowWindow($hwnd, 9) | Out-Null
        [WinApi]::SetForegroundWindow($hwnd) | Out-Null
        Write-Host "[INFO] PAD ウィンドウをフォーカスしました。"
    } else {
        Write-Warning "[WARN] PAD ウィンドウハンドルが取得できませんでした。"
    }
}

# ---- Ctrl+Shift+R を送信 ----
function Send-Shortcut {
    $wshell = New-Object -ComObject WScript.Shell
    $wshell.SendKeys("^+r")
    Write-Host "[INFO] Ctrl+Shift+R を送信しました。"
}

# ---- メイン処理 ----
$exePath = Find-PadExe

if (Test-PadRunning) {
    Write-Host "[INFO] PAD は既に起動しています。"
} else {
    Start-Pad -ExePath $exePath
    Write-Host "[INFO] $Wait 秒待機中..."
    Start-Sleep -Seconds $Wait
}

Set-PadWindowFocus
Start-Sleep -Milliseconds 500  # フォーカス移行を待つ
Send-Shortcut
