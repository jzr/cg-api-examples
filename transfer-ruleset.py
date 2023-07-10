"""
Copies a ruleset from one account into another.
Also works between datacenters.
"""

import cg_api

source = cg_api.Session(profile_name="source")
destination = cg_api.Session(profile_name="destination")

bundle_id = -142

ruleset = source.get(f"Compliance/Ruleset/{bundle_id}")

# The API will ignore read-only values, we don't have to clean up.
ruleset["name"] = "Transferred ruleset"

result = destination.post(f"Compliance/Ruleset", ruleset)

print(result["id"])
