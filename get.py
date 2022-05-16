# GET requests via Python3

from urllib import request
import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
url = input('Enter your URL: ')
cookie = input('Enter cookie: ')
contenttype = input('Enter Content-Type: ')
acceptlanguage = input ('Enter Accept-Language: ')
headers["Cookie"] = cookie
headers["Content-Type"] = contenttype
headers["Accept-Language"] = acceptlanguage 

response = requests.get(url, headers=headers)
#session = requests.Session()

print (response.text)
