"""
Update or create a generic list with values.
Can be used in GSL rules.
Or to use CloudGuard as a database.
"""

import cg_api

api = cg_api.Session()

generic_list_name = "Fruits_I_like"
values = ["Blueberry", "Pineapple", "Mango", "Cherry", "Lemon", "Pizza"]
items = [{"value": v} for v in values]

try:
    [generic_list] = [
        item for item in api.get("GenericList") if item["name"] == generic_list_name
    ]
    generic_list["items"] = items
    api.put("GenericList", generic_list)
except ValueError:
    generic_list = api.post("GenericList", {"name": generic_list_name, "items": items})

url = "https://portal.checkpoint.com/dashboard/cloudguard#/lists/generic/"
print(url + generic_list["id"])
