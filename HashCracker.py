import hashlib
import os
from colorama import Fore

os.system('clear')

print Fore.CYAN + '''
Select Your Type Hash:
---------------------
[1]MD5
[2]SHA1
[3]SHA224
[4]SHA256
[5]SHA384
[6]SHA512
---------------------
Coded By AlirezaC0d3r
'''
hashing = raw_input('Enter Your Hash : ' )

hashtype = raw_input('Enter Type Hash : ' )

file = raw_input('Enter Wordlist Exmple passlist.txt : ')

wordlist = open(file, 'r').readlines()

for password in wordlist:
    password = password.strip()

    if hashtype == '1':
        hash_a = hashlib.md5(password).hexdigest()

    elif typehash == '2':
        hash_a = hashlib.sha1(password).hexdigest()

    elif typehash == "3":
        hash_a = hashlib.sha224(password).hexdigest()

    elif typehash == "4":
        hash_a = hashlib.sha256(password).hexdigest()

    elif typehash == "5":
        hash_a = hashlib.sha384(password).hexdigest()
    elif typehash == "6":
        hash_a = hashlib.sha512(password).hexdigest()

    if hashing == hash_a:
        print Fore.GREEN + '_______________'
        print Fore.GREEN + '[!]Hash Cracked -> : ',password
        break
    else:
        print Fore.RED + '[*] Failed -> : ',password
