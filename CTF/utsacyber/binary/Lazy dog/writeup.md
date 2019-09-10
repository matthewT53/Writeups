# Lazy dog:

## Exploit notes:
* No binaries are provided
* Vulnerable to a **format string vulnerability**.
* To see the address printed by the first %p, we need to first send
136 junk bytes.

#### Find stack address of the return address (0x8048702):
* Loop through the address range of the stack looking for the bytes of
the return address shown in the debug message.
* In this case, we are searching for "\x02\x87\x48\x80".
* Wrote a script called find_stack_addr.py that does this and had to leave it
running overnight.
* The important stack addresses found by this script are shown below.

#### Stack addresses:
* The stack address that contains the first four a's of our input is 0xffffdad8.
* The stack address that contains the return address (0x8048702) is 0xffffda9c.
* The vulnerable function is probably a strcpy() because if there is a null
byte in the input then asterisks are printed.

#### Libc offsets:
* I am assuming the libc offsets are the same as the previous binary.
```c
offset___libc_start_main_ret = 0x18637
offset_system = 0x0003a940
offset_dup2 = 0x000d4b50
offset_read = 0x000d4350
offset_write = 0x000d43c0
offset_str_bin_sh = 0x15902b
```
* Also assuming the remote process has the same memory map as the previous binary:
```c
08048000-0804a000 r-xp 00000000 08:01 519128                             /home/user/pwn
0804a000-0804b000 r-xp 00001000 08:01 519128                             /home/user/pwn
0804b000-0804c000 rwxp 00002000 08:01 519128                             /home/user/pwn
0804c000-0806e000 rwxp 00000000 00:00 0                                  [heap]
f7e18000-f7e19000 rwxp 00000000 00:00 0
f7e19000-f7fc6000 r-xp 00000000 08:01 530352                             /lib32/libc-2.23.so
f7fc6000-f7fc7000 ---p 001ad000 08:01 530352                             /lib32/libc-2.23.so
f7fc7000-f7fc9000 r-xp 001ad000 08:01 530352                             /lib32/libc-2.23.so
f7fc9000-f7fca000 rwxp 001af000 08:01 530352                             /lib32/libc-2.23.so
f7fca000-f7fcd000 rwxp 00000000 00:00 0
f7fd3000-f7fd4000 rwxp 00000000 00:00 0
f7fd4000-f7fd7000 r--p 00000000 00:00 0                                  [vvar]
f7fd7000-f7fd9000 r-xp 00000000 00:00 0                                  [vdso]
f7fd9000-f7ffc000 r-xp 00000000 08:01 530345                             /lib32/ld-2.23.so
f7ffc000-f7ffd000 r-xp 00022000 08:01 530345                             /lib32/ld-2.23.so
f7ffd000-f7ffe000 rwxp 00023000 08:01 530345                             /lib32/ld-2.23.so
fffdd000-ffffe000 rwxp 00000000 00:00 0                                  [stack]
```
* We use 0xf7e19000 as the libc base address.
* By doing simple arithmetic we get:
    * System(): 0xf7e53940
    * "/bin/sh": 0xf7f7202b
    
* These assumptions were verified when I used a format string attack to get an
arbitrary read (%s) on 0xf7f7202b. Doing this, the remote binary printed
"/bin/sh".

## Goal:

## How to exploit:

## Scripts used:


## Flag:
CSACTF{th3_c0w_jumps_0v3r_the_m00n}
