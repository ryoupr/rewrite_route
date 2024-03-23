import subprocess
import json
import time


def start_instance(instance_id):
    res = subprocess.check_output(
        ["aws", "ec2", "start-instances", "--instance-ids", instance_id], timeout=60
    )
    res = res.decode()
    res = json.loads(res)
    while res["StartingInstances"][0]["CurrentState"]["Name"] != "running":
        res = subprocess.check_output(
            ["aws", "ec2", "start-instances", "--instance-ids", instance_id], timeout=60
        )
        time.sleep(5)
        res = res.decode()
        res = json.loads(res)

    return res
