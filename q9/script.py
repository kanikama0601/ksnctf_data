import requests
from requests.auth import HTTPDigestAuth
from hashlib import md5
import hashlib

import re

response=""

username="q9"
realm="secret"
uri="/q9/"
algorithm="MD5"
qop="auth"
nc="00000001"
cnonce="3c041a6fed175b2c"
method="GET:"+uri

encoded_a1 = "c627e19450db746b739f41b64097d449"
a2 = method
encoded_a2 = md5(a2.encode('utf-8')).hexdigest()

print(response)

# リクエストを送信
url = "http://ctfq.u1tramarine.blue/q9/flag.html"
response = requests.get(url)
if 'www-authenticate' in response.headers:
    auth_header = response.headers['www-authenticate']
    nonce = re.search('nonce="([^"]+)', auth_header).group(1)
else:
    print("WWW-Authenticate header not found")
    exit()
    
response_value = md5((f"{encoded_a1}:{nonce}:{nc}:{cnonce}:{qop}:{encoded_a2}").encode('utf-8')).hexdigest()

auth_header = f'Digest username=\"{username}\", realm=\"{realm}\", nonce=\"{nonce}\", uri=\"{uri}\", algorithm=\"{algorithm}\", qop=\"{qop}\", nc=\"{nc}\", cnonce=\"{cnonce}\", response=\"{response_value}\"'

responce = requests.get(url, headers={'Authorization': auth_header})

print(responce.status_code)
print(responce.text)