#!/usr/bin/env python

from pwn import *

xor_key = "082018"

url = "\x40\x08\x45\x03C\vTgPIn[_^T"
n = len(xor_key)

message = ""
for i in range(0, len(url)):
    c = ord(url[i])
    x = ord(xor_key[i % n])
    d = c ^ x

    message += str(chr(d))

print message
