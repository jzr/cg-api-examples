"""
Export a list of protected assets to CSV based on a filter.
The example filters all AWS IAM policies.
The values for the entity types appear to follow the pattern: "csp|EntityName".
"""

import csv

import cg_api
import tqdm


# The maximum page size is 1000. Smaller values are rarely useful outside of testing.
PAGE_SIZE = 1000

# A list of the fields we want to extract from each asset.
FIELDS = ["name"]

api = cg_api.Session()

payload = {"pageSize": PAGE_SIZE, "filter": {"includedEntityTypes": ["aws|IamPolicy"]}}

# The first call gives us the total number of results, and a _searchAfter_ token.
# We then need to loop until we have collected all assets.
# Every iteration, we update _searchAfter_ with the new value from the response.

data = api.post("protected-asset/search", payload)
total_count = data["totalCount"]

assets = [{k: v for k, v in asset.items() if k in FIELDS} for asset in data["assets"]]

# We skip the first page by starting from PAGE_SIZE, then iterate in steps of PAGE_SIZE
# until we reach total_count.
for _ in tqdm.tqdm(range(PAGE_SIZE, total_count, PAGE_SIZE)):
    # Every iteration we update the payload with a new _searchAfter_ index.
    payload["searchAfter"] = data["searchAfter"]
    data = api.post("protected-asset/search", payload)
    assets += [
        {k: v for k, v in asset.items() if k in FIELDS} for asset in data["assets"]
    ]

# Dump the results to a CSV.
with open("assets.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(assets)
