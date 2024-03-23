# Welcome to rewrite_route！！
AWS CLIを通じて対象インスタンスのパブリックIPをRoute53の対象ドメインのAレコードに登録するスクリプトです。
インスタンス起動時に実行するよう設定することでElasticIPの削減につながります。

# 設定方法
.env.txt ファイル内の事項を埋めて .env ファイルとして保存してください

# 動作要件
- AWS CLI が使用可能（おもにEC2、Route当たりの権限がついていること）
- AWS CLI のレスポンス形式がJSON形式であること。

