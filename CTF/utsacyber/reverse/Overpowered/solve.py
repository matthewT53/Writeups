#!/usr/bin/env python

from pwn import *

a = list(p32(0x191b0919))
b = list(p32(0x23211c0e))
c = list(p32(0x31052f6a))
d = list(p32(0x052d6a34))
e = list(p32(0x32393b37))
f = list(p32(0x53f346b))
g = list(p32(0x3d343b36))
h = list(p32(0x693d3b2f))

encoded_str = a + b + c + d + e + f + g + h + ['\x27']

XOR_KEY = 0x5a

decoded_str = ""

# print (encoded_str)
for c in encoded_str:
    d = ord(c) ^ XOR_KEY
    decoded_str += str(chr(d))

print decoded_str
