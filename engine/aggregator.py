def aggregate(findings):
    summary = {"CRITICAL":0,"HIGH":0,"MEDIUM":0,"LOW":0,"risk_score":0}
    for f in findings:
        summary[f["severity"]] += 1
        summary["risk_score"] += f["cvss"]
    return summary
