# SecAudit 🔐
### Automated Security Vulnerability Scanner with GitHub Actions

> Automatically scans websites for security vulnerabilities and raises GitHub Issues for each finding — just like a real security team's workflow.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-green)
![Security](https://img.shields.io/badge/Security-OWASP-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 What it does

- 🔍 **Scans** live websites for real security vulnerabilities
- 🚨 **Auto-creates GitHub Issues** for every vulnerability found with severity ratings
- ⚙️ **Runs automatically** on every code push via GitHub Actions
- 📊 **Generates JSON reports** with detailed findings
- 🔄 **Scheduled scans** every Monday 9am automatically

---

## 🛡️ Vulnerabilities Detected

| Check | Severity | OWASP Reference |
|---|---|---|
| Missing X-Frame-Options header | MEDIUM | A05: Security Misconfiguration |
| Missing Content-Security-Policy | MEDIUM | A05: Security Misconfiguration |
| Missing Strict-Transport-Security | MEDIUM | A02: Cryptographic Failures |
| Missing X-Content-Type-Options | MEDIUM | A05: Security Misconfiguration |
| No HTTPS enforcement | HIGH | A02: Cryptographic Failures |
| Insecure cookies (no Secure flag) | MEDIUM | A07: Identification Failures |
| Insecure cookies (no HttpOnly flag) | MEDIUM | A07: Identification Failures |

---

## 🏗️ Architecture

```
secaudit/
├── .github/
│   └── workflows/
│       └── security-scan.yml
├── scanner/
│   └── vulnerability_scanner.py
├── reports/
└── main.py
```

---

## ⚡ Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/hvarsh-cyber/secaudit.git
cd secaudit
```

**2. Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

**3. Run a scan**
```bash
python3 main.py
# Enter target URL when prompted
```

---

## 🤖 Automated Pipeline

Every push to `main` triggers:
1. Environment setup
2. Dependency installation
3. Security scan against target URL
4. Auto-creation of GitHub Issues for findings

To use in your own repo, add these GitHub secrets:
- `TARGET_URL` — the URL you want to scan
- `PAT_TOKEN` — your GitHub personal access token with repo scope

---

## 📊 Sample Output

```
SecAudit — Security Scanner
Target: https://example.com
==================================================
[✓] HTTPS is enabled
[!] MISSING: X-Frame-Options
[!] MISSING: Content-Security-Policy
[✓] GitHub Issue created: #1
[*] Total vulnerabilities found: 5
```

## 🔮 Roadmap

- [ ] Add SQL injection detection
- [ ] Add subdomain enumeration
- [ ] Slack/email alerting integration
- [ ] CVSS scoring for each vulnerability
- [ ] HTML report generation
- [ ] Docker containerisation

---

## 👩‍💻 Author

**Himavarsha Sathyanarayana**  
Master of Cybersecurity @ Monash University  
2.6 years Security Automation @ EchoStar/Dish Network (Fortune 500)  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://linkedin.com/in/himavarsh-s-0a215b213)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/hvarsh-cyber)

---

*Built as part of my cybersecurity portfolio. Inspired by real-world security automation work at EchoStar.*
