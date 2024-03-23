import json
import subprocess


def get_ec2_ip(instance_id):
    # 受け取ったインスタンスIDからそのインスタンスのパブリックIPを返す関数
    ec2_instances = subprocess.check_output(["aws", "ec2", "describe-instances"])
    ec2_instances = ec2_instances.decode()
    ec2_instances = json.loads(ec2_instances)
    for i in ec2_instances["Reservations"]:
        for j in i["Instances"]:
            if j["InstanceId"] == instance_id:
                for k in j["NetworkInterfaces"]:
                    ec2_public_ip_address = k["Association"]["PublicIp"]
                if ec2_public_ip_address is None:
                    return "Target ec2 instance don't have public ipv4 address."
                return ec2_public_ip_address
    return f"Target instance({instance_id}) is not found."
