#!/usr/bin/env python3
# Code by : 404 Not Found CyberSec

import argparse
import requests
from urllib.parse import urlparse

from core.headers import audit_headers
from core.tls import audit_tls
from core.methods import audit_methods
from core.exposure import audit_exposure
from core.behavior import audit_behavior

from engine.attack_surface import discover
from engine.aggregator import aggregate

from mapping.mitre import map_mitre

from reporting.reporter import display, save
from reporting.html import generate_html
from siem.logger import log_event


def banner():
    print("""
===========================================
        WEBGUARD SECURITY SCANNER
        Code by : 404 Not Found CyberSec
===========================================
""")


def main():
    banner()

    parser = argparse.ArgumentParser(
        description="WebGuard Advanced Security Scanner (Blue Team / SOC)"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Target URL (example: https://example.com)"
    )

    args = parser.parse_args()

    target_url = args.url.rstrip("/")
    response = requests.get(target_url, timeout=10)
    host = urlparse(target_url).hostname

    findings = []

    # Core security checks
    findings.extend(audit_headers(response))
    findings.extend(audit_tls(host))
    findings.extend(audit_methods(target_url))
    findings.extend(audit_exposure(target_url))
    findings.extend(audit_behavior(target_url))

    # Advanced attack surface discovery
    findings.extend(discover(target_url))

    # MITRE ATT&CK mapping
    for f in findings:
        mitre = map_mitre(f["title"])
        if mitre:
            f["mitre"] = mitre

    # Aggregate risk
    summary = aggregate(findings)

    # Output
    display(findings, summary)
    save(findings, summary)
    generate_html(findings, summary, target_url)

    # SIEM log
    log_event({
        "target": target_url,
        "summary": summary,
        "total_findings": len(findings)
    })


if __name__ == "__main__":
    main()
