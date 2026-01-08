from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

SEC_HEADERS = ["Content-Security-Policy","X-Frame-Options","X-Content-Type-Options"]

def audit_headers(resp):
    return [
        finding(
            "Missing security header",
            "HIGH",
            score("HIGH"),
            OWASP["Missing security header"],
            f"{h} missing",
            f"Add {h}"
        ) for h in SEC_HEADERS if h not in resp.headers
    ]
