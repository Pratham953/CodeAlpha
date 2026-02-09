#  Secure Coding Review – Internship Project

##  Project Overview
This project focuses on performing a **Secure Coding Review** of a Python Flask web application. 
The objective is to identify common security vulnerabilities through **manual code inspection** and **static analysis**, and then apply secure coding practices to remediate them.

The project demonstrates a complete **before-and-after security improvement workflow**, making it suitable for internship and academic evaluation.

---

##  Objectives
- Identify insecure coding practices
- Perform manual code review
- Use static analysis tools (Bandit)
- Document vulnerabilities professionally
- Implement secure remediation
- Follow secure coding best practices

---

##  Tools & Technologies
- Programming Language: Python
- Framework: Flask
- Static Analysis Tool: Bandit
- Operating System: Kali Linux
- IDE: VS Code
- Version Control: Git & GitHub

---

##  Methodology
1. Manual source code review
2. Identification of vulnerabilities
3. Static analysis using Bandit
4. Documentation of findings
5. Secure code remediation
6. Validation of fixes

---

##  Vulnerabilities Identified
- SQL Injection
- Hardcoded Secrets
- Plaintext Password Storage
- Debug Mode Enabled
- Lack of Input Validation

Detailed findings are available in:
reports/vulnerability_report.md

---

## Secure Remediation
- Implemented parameterized SQL queries
- Removed hardcoded credentials
- Used environment variables for secrets
- Disabled debug mode
- Added input validation

A secure version of the application is available in:
secure_app/

---

## Static Analysis
Bandit was used to perform static security analysis on the application source code.
The scan results were documented and used to validate secure remediation.

---

## Outcome
This project demonstrates practical understanding of:
- Secure coding principles
- Vulnerability assessment
- Static code analysis
- Secure remediation techniques



