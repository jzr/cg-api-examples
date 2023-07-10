"""
You tried transfer-ruleset.py but you do not have the ID anymore.
Now delete-ruleset.py is asking you for it.
"""

import cg_api

api = cg_api.Session(profile_name="destination")

rulesets = api.get("Compliance/Ruleset/view")

[bundle_id] = [
    ruleset["id"] for ruleset in rulesets if ruleset["name"] == "Transferred ruleset"
]

print(bundle_id)
