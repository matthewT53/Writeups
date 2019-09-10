#!/usr/bin/env python

import requests
import time
import re

hashes = []
hash = ""

for i in range(0, 30):
    print "[+] Requests: " + str(i)

    request_cookie = {"flag" : hash}
    r = requests.get("http://159.89.166.12:13500", cookies=request_cookie)
    hash = r.cookies["flag"]
    hashes.append(hash)

    time.sleep(0.1)

f = open("hashes.txt", "wb")

for hash in hashes:
    f.write(hash + "\n")

f.close()
