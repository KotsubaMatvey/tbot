$ErrorActionPreference = "Stop"

$AppDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogDir = Join-Path $AppDir "logs"
$PidFile = Join-Path $LogDir "bot.pid"
$StdoutLog = Join-Path $LogDir "bot_runtime.out.log"
$StderrLog = Join-Path $LogDir "bot_runtime.err.log"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

if (Test-Path $PidFile) {
    $ExistingPid = Get-Content $PidFile -Raw
    $ExistingPid = $ExistingPid.Trim()
    if ($ExistingPid -and (Get-Process -Id ([int]$ExistingPid) -ErrorAction SilentlyContinue)) {
        Write-Host "Bot already running. PID=$ExistingPid"
        exit 0
    }
}

$Python = (Get-Command python -ErrorAction Stop).Source
$Process = Start-Process `
    -FilePath $Python `
    -ArgumentList @("-u", "bot.py") `
    -WorkingDirectory $AppDir `
    -RedirectStandardOutput $StdoutLog `
    -RedirectStandardError $StderrLog `
    -WindowStyle Hidden `
    -PassThru

Write-Host "Bot starting. Bootstrap PID=$($Process.Id)"
Write-Host "Logs:"
Write-Host "  stdout: $StdoutLog"
Write-Host "  stderr: $StderrLog"
