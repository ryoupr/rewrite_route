import json
import subprocess as sp


def rewrite_route(DOMAIN_NAME, SUB_NAME, HOSTED_ZONE_ID, IP_ADDRESS):
    BATCH_JSON = {
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": f"{SUB_NAME}.{DOMAIN_NAME}",
                    "Type": "A",
                    "TTL": 300,
                    "ResourceRecords": [{"Value": IP_ADDRESS}],
                },
            }
        ]
    }
    BATCH_JSON = json.dumps(BATCH_JSON)

    command = [
        "aws",
        "route53",
        "change-resource-record-sets",
        "--hosted-zone-id",
        f"{HOSTED_ZONE_ID}",
        "--change-batch",
        f"{BATCH_JSON}",
    ]

    print(command)

    sp.call(command)
