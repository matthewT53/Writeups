#!/usr/bin/env python

from z3 import *

r1 = int(raw_input("r1: "))
r2 = int(raw_input("r2: "))
r3 = int(raw_input("r3: "))

x, y, z = BitVecs("x y z", 32)

s = Solver()

s.add(x < 0, y < 0, x + y == r1)
s.add(y < 0, z < 0, y + z == r2)
s.add(x < 0, z < 0, x + z == r3)

if s.check():
    print s.model()
    print "x: " + int(m[x], 32)
