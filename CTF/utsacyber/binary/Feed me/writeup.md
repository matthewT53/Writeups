# Feed me

## Protections:
* No protections are turned on and server has no ASLR.
* Doesn't mean its a shellcode challenge.

## Exploit notes:
#### Buffer overflow vulnerability:
* There is a function called pwnme() that we need to somehow jump to.
* The buffer that we can read() into is only 0x32 bytes in size however we read
in 0x46 bytes.

#### Pseudo canary bypass:
* There is a canary like password thing we need to bypass.
* We just need to add the string "utsa" into our overflow. This is done at an
offset of 0x32 bytes in our exploit.

#### Control over RBP:
* With our overflow exploit, we can also overwrite the saved EBP that is on
the stack.
* A snapshot of the stack before the call to read() is shown below:

0xffffd050:	0xf7fb3d60	0xffffd0f4	0xf7fb3000	0x00000016
0xffffd060:	0xffffffff	0xf7fb3000	0xf7e0be18	0xf7fd21b0
**0xffffd070**:	0xf7fb3000	0xffffd154	0xf7ffcd00	0x00040000
0xffffd080:	0x00000007	0x00000002	0xf7e2d880	0x0804866b
0xffffd090:	0x00000001	0xffffd154	**0x61737475**	0x00000034
0xffffd0a0:	0xf7fb33dc	0x08048250	**0xffffd0b8**	0x08048614
0xffffd0b0:	0x00000001	0xf7fb3000	0x00000000	0xf7e17286
0xffffd0c0:	0x00000001	0xffffd154	0xffffd15c	0x00000000

The vulnerable buffer starts at address 0xffffd066 and continues to 0xffffd0ac
which is the return address for pwnme()'s stack frame.

Note, the canary and the saved EBP are shown in bold.

* The saved EBP value should be changed to somewhere at the start of our buffer. We chose
to use "vuln_buffer+0xa" which is 0xffffd070.

#### Fake stack frame:
* After modifying the saved EBP value, once the program returns to main() from
pwnme(), EBP will now be 0xffffd070.
* At the address 0xffffd070, the value "bbbb" should be stored to represent a dummy
RBP value. Also, at 0xffffd074, we want to have the address of win().
* Once the program returns from main(), EBP will have "bbbb" and the program will
return to win().

## The exploit:
* "a" * 0xa + "bbbb" + addr of win() + "c" * 0x20 + "utsa" + "d" * padding +
addr of new rbp.

## Scripts used:
* See exploit.py
