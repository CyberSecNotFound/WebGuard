def finding(title, severity, cvss, owasp, description, recommendation):
    return {
        "title": title,
        "severity": severity,
        "cvss": cvss,
        "owasp": owasp,
        "description": description,
        "recommendation": recommendation
    }
