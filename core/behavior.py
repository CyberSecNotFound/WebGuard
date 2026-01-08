import requests
from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

def audit_behavior(url):
    r = requests.get(url, headers={"X-Forwarded-For":"127.0.0.1"})
    if "localhost" in r.text.lower():
        return [finding(
            "Trust boundary violation",
            "CRITICAL",
            score("CRITICAL"),
            OWASP["Trust boundary violation"],
            "Spoofed header trusted",
            "Validate proxy headers"
        )]
    return []
