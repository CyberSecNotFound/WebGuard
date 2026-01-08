def score(severity):
    return {
        "LOW": 3.1,
        "MEDIUM": 5.5,
        "HIGH": 7.5,
        "CRITICAL": 9.8
    }.get(severity, 0)
