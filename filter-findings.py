"""
Find all findings for a specific rule ID.
"""

import cg_api


def paginate_findings(session, filter, pageSize=10):
    findings = []

    payload = {"filter": filter, "dataSource": "Finding"}
    data = session.post("Compliance/Finding/search", payload)

    findings += data["findings"]

    total_count = data["totalFindingsCount"]

    while len(findings) < total_count:
        payload["searchAfter"] = data["searchAfter"]
        data = session.post("Compliance/Finding/search", payload)
        findings += data["findings"]

    return findings


def main():
    api = cg_api.Session()
    findings_filter = {"fields": [{"name": "ruleId", "value": "D9.AWS.NET.04"}]}

    findings = paginate_findings(api, findings_filter)

    for finding in findings:
        print(finding["severity"], finding["id"], finding["ruleName"])


if __name__ == "__main__":
    main()
