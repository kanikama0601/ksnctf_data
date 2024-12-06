import requests
from requests.auth import HTTPDigestAuth
from hashlib import md5
import re

url = 'http://ctfq.u1tramarine.blue/q9/flag.html'

#　事前にリクエストを送信
response = requests.get(url)
auth_header = response.headers['WWW-Authenticate']

print("auth_header:\n"+auth_header+"\n")

# リクエストヘッダーから情報を抽出&いろいろ定義
cnonce = "chinchin"
nc = "00000001"
nonce = re.search('nonce="([^"]+)', auth_header).group(1)

print("nonce:"+nonce+"\n")

md5_a2 = md5('GET:/q9/flag.html'.encode("utf-8")).hexdigest()
auth_response = md5(f'c627e19450db746b739f41b64097d449:{nonce}:{nc}:{cnonce}:auth:{md5_a2}'.encode("utf-8")).hexdigest()
print(auth_response)

data = f'Digest username="q9", realm="secret", nonce="{nonce}", uri="/q9/flag.html", algorithm="MD5", qop="auth", nc="{nc}", cnonce="{cnonce}", response="{auth_response}"'
print(data)

response = requests.get(url, headers={'Authorization': data})

print(response.text)