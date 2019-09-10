#!/usr/bin/env python

xor_str = "\x13\x13eg#v\t\x05\x0f#HE\x04CC\x07\x0f0V\x14\x15\\\x17\t\x0f2AU\x02\x01\x00\x01#\x1fE{\x14\\\x13\x17#qG{\x04\x00\x1e\x11$q\x14J\n"

keys = "P@$$w0rd"

decoded_str = ""
for i in range(0, len(xor_str)):
    c = xor_str[i]
    x = ord(c)
    k = ord(keys[i % len(keys)])
    d = x ^ k
    decoded_str += chr(d)

print decoded_str
