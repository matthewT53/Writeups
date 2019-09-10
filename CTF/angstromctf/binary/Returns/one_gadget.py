#!/usr/bin/env python

from one_gadget import generate_one_gadget

path_to_libc = "libc.so.6"

for offset in generate_one_gadget(path_to_libc):
    print (offset)
