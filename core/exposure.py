import requests
from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

def audit_exposure(url):
    return [
        finding(
            "Sensitive path exposed",
            "CRITICAL",
            score("CRITICAL"),
            OWASP["Sensitive path exposed"],
            f"{p} accessible",
            "Restrict access"
        )
        for p in ["/.env","/.git"] if requests.get(url+p).status_code==200
    ]
