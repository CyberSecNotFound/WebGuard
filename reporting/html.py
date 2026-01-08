import json
from datetime import datetime

def generate_html(findings, summary, target):
    rows = ""
    for f in findings:
        rows += f"""
        <tr>
            <td>{f['severity']}</td>
            <td>{f['title']}</td>
            <td>{f['owasp']}</td>
            <td>{f['cvss']}</td>
            <td>{f['description']}</td>
        </tr>
        """

    posture = max(0, 100 - summary["risk_score"])

    html = f"""
    <html>
    <head>
        <title>WebGuard Security Report</title>
        <style>
            body {{ font-family: Arial; padding:20px; }}
            table {{ width:100%; border-collapse:collapse; }}
            th, td {{ border:1px solid #ccc; padding:8px; }}
            th {{ background:#222; color:white; }}
        </style>
    </head>
    <body>
        <h1>WebGuard Executive Security Report</h1>
        <p><b>Target:</b> {target}</p>
        <p><b>Date:</b> {datetime.utcnow()}</p>
        <h2>Security Posture Score: {posture}/100</h2>

        <h2>Risk Summary</h2>
        <pre>{json.dumps(summary, indent=4)}</pre>

        <h2>Findings</h2>
        <table>
            <tr>
                <th>Severity</th>
                <th>Title</th>
                <th>OWASP</th>
                <th>CVSS</th>
                <th>Description</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    with open("reports/webguard.html", "w") as f:
        f.write(html)
