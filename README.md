# Web Application Vulnerability Scanner 

A Python-based tool to scan web applications for common vulnerabilities like:

- ✅ Cross-Site Scripting (XSS)
- ✅ SQL Injection (SQLi)

Built as part of the Elevate Labs Cybersecurity Internship (June 2025), this project automates the process of finding insecure input fields in websites and tests them with basic payloads.

---

## Features

- Scans webpages for HTML forms
- Detects `GET` and `POST` methods
- Injects malicious payloads into text fields
- Identifies reflected payloads in server responses
- Supports testing against intentionally vulnerable test sites

---

## Tools & Technologies

- Python 3
- `requests` – send HTTP requests
- `BeautifulSoup` – parse HTML
- `urllib.parse` – handle URLs

---

## How to Run

### 1. Clone or download this repository
```bash
git clone https://github.com/your-username/web-vulnerability-scanner.git
cd web-vulnerability-scanner
