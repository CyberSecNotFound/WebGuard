MITRE = {
    "Sensitive path exposed": ("Initial Access", "T1190"),
    "Weak TLS version": ("Credential Access", "T1557"),
    "Trust boundary violation": ("Defense Evasion", "T1070")
}

def map_mitre(title):
    if title == "Sensitive path exposed":
        return {
            "tactic": "Initial Access",
            "technique": "T1190 – Exploit Public-Facing Application"
        }
    if title == "Trust boundary violation":
        return {
            "tactic": "Defense Evasion",
            "technique": "T1070 – Indicator Removal"
        }
    return None

