# PowerShell script to run test suite for CI/CD on Windows

Write-Host "=== Pink Morsels Sales Visualizer - Test Suite ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Activating virtual environment..." -ForegroundColor Yellow
if (Test-Path ".venv\Scripts\Activate.ps1") {
    & .venv\Scripts\Activate.ps1
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Virtual environment not found at .venv\" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Step 2: Running test suite..." -ForegroundColor Yellow
Write-Host ""

python -m pytest test_appv1.py -v

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "===================================" -ForegroundColor Green
    Write-Host "[SUCCESS] All tests passed!" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Green
    exit 0
} else {
    Write-Host ""
    Write-Host "===================================" -ForegroundColor Red
    Write-Host "[FAILED] Tests failed!" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
    exit 1
}
