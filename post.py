import requests
from requests.structures import CaseInsensitiveDict

url = "http://ptl-bac98832-e4681219.libcurl.so/pentesterlab"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
# headers["Content-Length"] = "10"
data = ""

response = requests.post(url, headers=headers, data=data)

print(response.text)
