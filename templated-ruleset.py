"""
Creates a ruleset to check for mandatory tags for a list of entities.
A single rule is created for each entity + tag combination.
"""

import cg_api


def make_rule(entity_name, tag_name):
    return {
        "name": f"{entity_name} must have tag '{tag_name}'",
        "description": "Generated rule for required tags",
        "severity": "Critical",
        "logic": f"{entity_name} should have tags contain [ key = '{tag_name}' ]",
    }


tag_names = ["owner", "data-classification", "accessibility"]
entity_names = [
    "Instance",
    "Lambda",
    "S3Bucket",
    "ELB",
    "ApiGateway",
    "CloudFront",
    "EKSCluster",
    "AppSync",
]

rules = [
    make_rule(entity_name, tag_name)
    for tag_name in tag_names
    for entity_name in entity_names
]

ruleset = {
    "rules": rules,
    "name": "Templated ruleset",
    "description": "Example ruleset from template",
    "cloudVendor": "aws",
}

api = cg_api.Session()

print(api.post("Compliance/Ruleset", ruleset)["id"])
