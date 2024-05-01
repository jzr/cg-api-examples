"""
Check if an AWS key belongs to an onboarded account.
"""

import base64
import binascii
import sys

import cg_api


def AWSAccount_from_AWSKeyID(AWSKeyID):
    # from https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489
    # via https://cloud.hacktricks.xyz/pentesting-cloud/aws-security/aws-services/aws-security-and-detection-services/aws-cloudtrail-enum

    trimmed_AWSKeyID = AWSKeyID[4:]  # remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID)  # base32 decode
    y = x[0:6]

    z = int.from_bytes(y, byteorder="big", signed=False)
    mask = int.from_bytes(
        binascii.unhexlify(b"7fffffffff80"), byteorder="big", signed=False
    )

    e = (z & mask) >> 7
    return str(e)


api = cg_api.Session()
account_id = AWSAccount_from_AWSKeyID(sys.argv[1])

for account in api.get("CloudAccounts"):
    if account["externalAccountNumber"] == account_id:
        print(f"The key belongs to an onboarded AWS account: {account['name']}")
        break
else:
    print("The key doesn't belong to any onboarded AWS accounts")
