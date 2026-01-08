# WebGuard

**WebGuard** is an advanced web security scanning tool designed for **Blue Team, SOC Analysts, Security Engineers, and Infrastructure Security professionals**. It performs passive and active security analysis, maps findings to **OWASP Top 10**, **MITRE ATT&CK**, calculates **CVSS-based risk scores**, generates **executive HTML reports**, and outputs **SIEM-ready logs**.

---

## 🚀 Features

* Advanced HTTP Security Header Analysis
* TLS / SSL Inspection
* HTTP Method & Exposure Analysis
* Behavior & Attack Surface Discovery
* OWASP Top 10 Mapping
* MITRE ATT&CK Mapping
* CVSS Risk Scoring & Aggregation
* Executive HTML Dashboard
* JSON Report for SIEM (ELK / Wazuh / Splunk)
* Linux-first (Kali / Ubuntu / Server)

---

## 📦 Requirements

* Linux (Kali Linux recommended)
* Python **3.9+**
* Internet access for target scanning

---

## 🔧 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/webguard.git
cd webguard
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic Scan

```bash
python3 webguard.py --url https://example.com
```

### Output Files

```bash
reports/webguard.json
reports/webguard.html
```

Open HTML report:

```bash
firefox reports/webguard.html
```

---

## 📊 SIEM Integration Example

```bash
python3 webguard.py --url https://example.com >> /var/log/webguard.log
```

Compatible with:

* ELK Stack
* Wazuh
* Splunk

---

## 🐳 Docker Deployment

```bash
docker build -t webguard .
docker run -it webguard python3 webguard.py --url https://example.com
```

---

## 👨‍💻 Author

**Code by:** 404 Not Found CyberSec
**Field:** Cybersecurity | Blue Team | SOC | Security Engineering

---

## ⚠️ Disclaimer

WebGuard is intended for **authorized security testing only**. Always ensure you have permission before scanning any target.

---

## ⭐ Portfolio Statement

> Designed and implemented an enterprise-grade web security scanning platform with executive reporting, SIEM integration, OWASP and MITRE mapping, and CVSS-based risk scoring.
