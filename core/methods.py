import requests
from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

def audit_methods(url):
    results=[]
    for m in ["PUT","DELETE"]:
        if requests.request(m,url).status_code < 405:
            results.append(
                finding(
                    "Dangerous HTTP method",
                    "HIGH",
                    score("HIGH"),
                    OWASP["Dangerous HTTP method"],
                    f"{m} enabled",
                    "Restrict HTTP methods"
                )
            )
    return results
