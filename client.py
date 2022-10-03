import requests
from requests.auth import HTTPDigestAuth

url = 'http://127.0.0.1:5000/'
r = requests.get(url + 'ping', auth=HTTPDigestAuth('vcu', 'rams'))
print(r.text, 'from client')