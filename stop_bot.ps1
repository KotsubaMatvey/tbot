$ErrorActionPreference = "Stop"

$AppDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogDir = Join-Path $AppDir "logs"
$PidFile = Join-Path $LogDir "bot.pid"

if (-not (Test-Path $PidFile)) {
    Write-Host "No bot pid file found."
    exit 0
}

$PidText = (Get-Content $PidFile -Raw).Trim()
if (-not $PidText) {
    Remove-Item $PidFile -Force
    Write-Host "Empty pid file removed."
    exit 0
}

$BotPid = [int]$PidText
$Process = Get-Process -Id $BotPid -ErrorAction SilentlyContinue
if ($Process) {
    Stop-Process -Id $BotPid -Force
    Write-Host "Bot stopped. PID=$BotPid"
} else {
    Write-Host "Bot process is not running. PID=$BotPid"
}

Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
