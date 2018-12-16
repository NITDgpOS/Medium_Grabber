#!/usr/bin/python3

import os
import os.path
from os import listdir
from os.path import isfile, join
import getpass
from Crypto import Random
from Crypto.Cipher import AES

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)


def clear(): return os.system('clear')

flag = 1 # if flag = 1, then we need to decrypt. Else no decryption needed

if not os.path.isfile('creds.ge.enc'):  # Check if the credentials are saved
    clear()
    username = str(input("Enter your email or registered phone number: "))
    password = str(getpass.getpass("Enter your password: "))
    while(1):
        remember = str(input("Do you want to save your credentials? (Y/N): "))
        if remember == 'N' or remember == 'n':
            flag = 0
            break
        elif remember == 'Y' or remember =='y':
            f = open("creds.ge", "w+")
            f.write(username + '\n')
            f.write(password)
            f.close()
            enc.encrypt_file("creds.ge")
            print("Credentials Saved.")
            break
        else:
            print("Wrong input chosen")
            continue

if(flag):
    enc.decrypt_file("creds.ge.enc")
    p = ''
    with open("creds.ge", "r") as f:
        p = f.readlines()
    username = p[0].replace('\n','')
    password = p[1]
    enc.encrypt_file("creds.ge")
