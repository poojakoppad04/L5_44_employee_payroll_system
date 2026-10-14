# L5_44_employee_payroll_system

## Software Engineering Lab 5 — Static Code Analysis

### Project Overview
This project demonstrates static code analysis on a Python-based employee payroll system. It uses static analysis tools to identify potential code quality issues, coding standard violations, and security concerns.

### Objectives
- Analyze Python source code using static analysis tools.
- Identify potential bugs, code quality issues, and security risks.
- Document findings and improvements.
- Compare analysis reports before and after modifications.

### Tools Used
- **Pylint:** Checks Python code quality and coding conventions.
- **Bandit:** Identifies potential security issues in Python code.
- **Flake8:** Checks Python style and common programming errors.

### Repository Contents

| File | Description |
|---|---|
| `employee_payroll_system.py` | Python employee payroll system |
| `employee_payroll_system_original.py` | Original version of the source code |
| `pylint_report.txt` | Initial Pylint report |
| `pylint_report_after.txt` | Pylint report after modifications |
| `bandit_report.txt` | Initial Bandit report |
| `bandit_report_after.txt` | Bandit report after modifications |
| `flake8_report.txt` | Initial Flake8 report |
| `flake8_report_after.txt` | Flake8 report after modifications |
| `issues.md` | Documented code analysis issues |
| `reflection.md` | Reflection on the lab and analysis process |
| `Lab 5_Static_Analysis_Report.docx` | Lab report and documentation |

### How to Run the Analysis

Ensure Python and the required tools are installed.

Install the tools:

```bash
python -m pip install pylint bandit flake8
```

Navigate to the directory containing `employee_payroll_system.py` and run:

```bash
python -m pylint employee_payroll_system.py
python -m bandit employee_payroll_system.py
python -m flake8 employee_payroll_system.py
```

### Results
The project includes initial and post-modification reports for all three analysis tools. The final reports document the outcomes of the static analysis process.

### Conclusion
This lab demonstrates how static analysis tools can help assess Python code quality, maintain coding standards, and identify potential security concerns before execution.

---
Software Engineering Lab 5
