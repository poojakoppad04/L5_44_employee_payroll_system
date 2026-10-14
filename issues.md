# Lab 5: Static Code Analysis — Issue Documentation

| Sl. No. | Issue Identified | Tool | Severity | Fix Implemented |
|---|---|---|---|---|
| 1 | Mutable default argument (`transaction_logs=[]`) | Pylint | Warning | Changed the default value to `None` and initialized the list inside the function. |
| 2 | Bare `except` block with `pass` | Pylint, Bandit, Flake8 | Low | Removed the broad exception handler and implemented input validation and logging. |
| 3 | Unsafe `eval()` function | Pylint, Bandit | Medium | Replaced dynamic expression evaluation with validated numeric tax-rate calculations. |
| 4 | Weak MD5 hashing algorithm | Bandit | High | Replaced MD5 with SHA-256 to generate the employee ID digest. |
| 5 | `random.randint()` used for token generation | Bandit | Low | Replaced it with the `secrets` module. |
| 6 | `os.system()` used to execute a shell command | Bandit | High | Removed shell command execution and used Python logging instead. |
| 7 | File opened without explicit encoding or context manager | Pylint | Warning | Used `Path.open()` with UTF-8 encoding and a `with` statement. |
| 8 | Unused imports and variables | Pylint, Flake8 | Warning | Removed unused imports and variables. |
| 9 | Non-standard function naming and missing docstrings | Pylint | Convention | Renamed `processSalary()` to `process_salary()` and added docstrings. |
| 10 | Incorrect `None` comparison and unnecessary conditional logic | Pylint, Flake8 | Convention | Replaced `== None` with `is None` and simplified the conditional logic. |
| 11 | Hardcoded payroll secret exposed through output | Manual review | Security concern | Removed the hardcoded secret and stopped printing it. |
| 12 | Inconsistent line endings | Pylint | Formatting | Normalized line endings and reran the analysis tools. |

## Analysis Results

| Tool | Before Fixing | After Fixing |
|---|---|---|
| Pylint | 5.32/10 | 10.00/10 |
| Bandit | 5 issues identified | No issues identified |
| Flake8 | Multiple violations | No violations reported |
