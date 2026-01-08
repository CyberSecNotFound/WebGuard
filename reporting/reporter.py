import json

def display(findings, summary):
    print("\n====== WEBGUARD SECURITY REPORT ======\n")
    for f in findings:
        print(f"[{f['severity']}] {f['title']}")
        print(f" OWASP : {f['owasp']}")
        print(f" CVSS  : {f['cvss']}")
        print(f" DESC  : {f['description']}")
        print(f" FIX   : {f['recommendation']}")
        if "mitre" in f:
            print(f" MITRE : {f['mitre']['tactic']} / {f['mitre']['technique']}")
        print()

    print("=== RISK SUMMARY ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

def save(findings, summary):
    with open("reports/webguard.json", "w") as f:
        json.dump({"findings": findings, "summary": summary}, f, indent=4)
