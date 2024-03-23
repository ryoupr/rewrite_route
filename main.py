import os
import sys
from libs.get_ec2_ip import get_ec2_ip
from libs.rewrite_route import rewrite_route
from libs.start_instance import start_instance
from libs.is_env_file_in_directory import is_env_file_in_directory
from dotenv import load_dotenv

# 環境変数読み込み
if is_env_file_in_directory(".env") == True:
    load_dotenv()
else:
    print(".env ファイルが存在するか確認してください。\n初期状態では .env.txt となっているので注意してください。")
    sys.exit(1)


# main.pyが存在するディレクトリのパスを取得
current_dir = os.path.dirname(os.path.realpath(__file__))

# start_instance.pyなどの他のスクリプトを読み込む
start_instance_path = os.path.join(current_dir, 'libs', 'start_instance.py')



if __name__ == "__main__":

    DOMAIN_NAME = os.getenv("DOMAIN_NAME")
    HOSTED_ZONE_ID = os.getenv("HOSTED_ZONE_ID")
    INSTANCE_ID = os.getenv("INSTANCE_ID")

    start_instance(INSTANCE_ID)
    IP_ADDRESS = get_ec2_ip(INSTANCE_ID)
    rewrite_route(DOMAIN_NAME, INSTANCE_ID, HOSTED_ZONE_ID, IP_ADDRESS)
