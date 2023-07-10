"""
You've played around with transfer-ruleset.py and need to get rid of the result.
Pass in the ruleset ID as the first argument.
"""

import sys

import cg_api

api = cg_api.Session(profile_name="destination")

bundle_id = sys.argv[1]
api.delete(f"Compliance/Ruleset/{bundle_id}")
