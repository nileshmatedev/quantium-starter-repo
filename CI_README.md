# Continuous Integration (CI) Scripts

This directory contains scripts for automated testing in CI/CD environments.

## Scripts

### `run_tests.sh` (Bash - Linux/macOS/CI)
Bash script for running tests on Unix-based systems and CI platforms like GitHub Actions.

**Usage:**
```bash
chmod +x run_tests.sh
./run_tests.sh
```

**What it does:**
1. Activates the Python virtual environment at `.venv/`
2. Runs the test suite using pytest
3. Returns exit code 0 if all tests pass
4. Returns exit code 1 if any test fails or an error occurs

### `run_tests.ps1` (PowerShell - Windows)
PowerShell script for running tests on Windows systems.

**Usage:**
```powershell
powershell -ExecutionPolicy Bypass -File .\run_tests.ps1
```

Or if execution policy allows:
```powershell
.\run_tests.ps1
```

**What it does:**
1. Activates the Python virtual environment at `.venv\`
2. Runs the test suite using pytest
3. Returns exit code 0 if all tests pass
4. Returns exit code 1 if any test fails or an error occurs

## GitHub Actions Workflow

The `.github/workflows/test.yml` file configures automated testing on GitHub:
- Runs on every push to main/master branch
- Runs on every pull request
- Sets up Python environment
- Installs dependencies
- Executes test suite using `run_tests.sh`

## Exit Codes

Both scripts follow standard Unix exit code conventions:
- **0**: Success (all tests passed)
- **1**: Failure (tests failed or error occurred)

This allows CI systems to automatically detect test failures and take appropriate action.
