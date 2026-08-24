# validate-framework.ps1 — Windows PowerShell wrapper for validate-framework.py
#
# Usage:
#   .\scripts\validate-framework.ps1
#   .\scripts\validate-framework.ps1 -RepoRoot "D:\Projects\My-consulting-startup-business\AQEVON\ai-native-architecture"
#
# Requires Python 3 with pyyaml installed (pip install pyyaml).

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"

function Test-PythonAvailable {
    try {
        $null = Get-Command python -ErrorAction Stop
        return "python"
    } catch {
        try {
            $null = Get-Command python3 -ErrorAction Stop
            return "python3"
        } catch {
            Write-Error "Python is not installed or not on PATH. Install Python 3 to run this validation script."
            exit 2
        }
    }
}

$pythonCmd = Test-PythonAvailable

Write-Host "Running AQEVON framework validation against: $RepoRoot" -ForegroundColor Cyan

$scriptPath = Join-Path $PSScriptRoot "validate-framework.py"

& $pythonCmd $scriptPath --repo-root $RepoRoot
$exitCode = $LASTEXITCODE

if ($exitCode -eq 0) {
    Write-Host "`nValidation passed." -ForegroundColor Green
} else {
    Write-Host "`nValidation FAILED. See errors above." -ForegroundColor Red
}

exit $exitCode
