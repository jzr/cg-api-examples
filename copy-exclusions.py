"""
Copies exclusions from one ruleset to another.
Exclusions that don't have matching rules in the target ruleset have no effect.
"""

import cg_api

api = cg_api.Session()

from_bundle = -142
to_bundle = 16528

exclusions = api.get(f"Compliance/Exclusion")

for exclusion in exclusions:
    if exclusion["rulesetId"] == from_bundle:
        exclusion["rulesetId"] = to_bundle
        exclusion["comment"] += f"\nCopied from ruleset {from_bundle}"

        api.post(f"Compliance/Exclusion", exclusion)
