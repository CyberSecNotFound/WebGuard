import ssl, socket
from utils.risk import finding
from reporting.cvss import score
from mapping.owasp import OWASP

def audit_tls(host):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host,443),5) as s:
            with ctx.wrap_socket(s, server_hostname=host) as tls:
                if tls.version() in ["TLSv1","TLSv1.1"]:
                    raise Exception("Weak TLS")
    except:
        return [finding(
            "Weak TLS version",
            "CRITICAL",
            score("CRITICAL"),
            OWASP["Weak TLS version"],
            "TLS insecure",
            "Enforce TLS 1.2+"
        )]
    return []
