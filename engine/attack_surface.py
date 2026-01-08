import requests
from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

COMMON = ["/backup.zip","/.git","/admin"]

def discover(url):
    results = []
    for p in COMMON:
        if requests.get(url+p).status_code == 200:
            results.append(
                finding(
                    "Attack surface exposure",
                    "HIGH",
                    score("HIGH"),
                    OWASP["Attack surface exposure"],
                    f"{p} exposed",
                    "Remove unused files"
                )
            )
    return results
