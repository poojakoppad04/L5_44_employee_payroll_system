# Lab 5: Static Code Analysis — Reflection

## 1. Define static code analysis.

Static code analysis means analyzing the source code of an application without executing it. It identifies coding errors, coding-standard violations, and potential security vulnerabilities.

## 2. Tell the difference between Pylint, Bandit, and Flake8.

Pylint inspects code quality, variable naming, variable usage, and programming practices. Bandit scans for potential security vulnerabilities in Python code, while Flake8 checks coding style and reports common code-quality violations.

## 3. What problems can be found in the employee payroll system?

The analysis identified problems such as mutable default arguments, unsafe use of eval(), weak MD5 hashing, insecure random token generation, shell command execution, poor exception handling, unused variables, and file-handling issues.

## 4. How were the discussed bugs fixed?

The issues were addressed by using safe default arguments, validating input values, replacing eval() with direct calculations, employing SHA-256 hashing and the secrets module, removing shell command execution, improving file handling, and following Python naming and documentation conventions.

## 5. After fixing the bugs, what were the results?

After fixing the issues, the Pylint score improved from 5.32/10 to 10.00/10. Bandit reported no remaining issues, and Flake8 reported no violations.

## 6. What did you learn in this lab?

This lab helped me understand the importance of static analysis in improving code quality and security. I learned how Pylint, Bandit, and Flake8 can identify different problems and how to apply appropriate fixes to make a Python program more readable, maintainable, and secure.

## Conclusion

Static code analysis was performed on the employee payroll system using Pylint, Bandit, and Flake8. The identified code-quality and security issues were addressed, and the program was analyzed again to verify the improvements. The results demonstrated improved code quality, although static analysis alone cannot guarantee complete security.
