# armoury:

## Program protections:
* NX
* ASLR
* PIE
* Canary
* Anti-debugging techniques.

## Vulnerabilities:
1. Format string vulnerability.
2. Buffer overflow vulnerability.

## Anti-debug disarm:
* To disable the anti-debugging, nop out the call to initialize().

## Binary notes:
* The program asks for the name of a rifle twice. This input is vulnerable to
a format string attack.
* Finally the program asks the user for feedback which is vulnerable to a
stack overflow attack.

## Exploit notes:
### Canary leak:
* It takes around 13 %p's to leak the value of the canary.
* We need to leak the canary on the first input and then leak the PIE address
the second time we input because if we try to leak both at the same time, the
format string will overwrite the canary value.

### PIE leak:
* The PIE address that we need lies next to the next the canary.
* The PIE address on the stack is the address of libc_csu_init().
* libc_csu_init() has PIE offset of 0xca0.

### Libc address leaks:
* We will use puts() to leak the address of fgets() and printf().
* puts() has a code offset of 0x810.
* Use libc database to find offsets to system() and "/bin/sh".

### Stack overflow:
* After the program asks if we have any input, a scanf() is called to receive
our input however scanf() is unbounded.
* The offset from the start of the buffer given to scanf() to the return address
is 0x20 bytes. i.e "a" * 0x19 + "\x00"

### Exploit challenges:
* Sometimes the addresses have a 0xd byte in them which scanf() doesn't like.
Scanf() ignores all the bytes after 0xd.

## Steps to exploit:
1. Send 13 %p's to leak the canary as the first rifle name.
2. Send 14 %p's to leak an address in the code (PIE leak) as the second rifle name.
3. Calculate the address of puts(), printf() and fgets().
4. Exploit the buffer overflow to leak the address of printf() and fgets(). Also
calculate the address of the ROP gadget:
```c
    pop rdi; ret;
```
5. Use these leaks to find the libc version.
6. Find the address of system() and "/bin/sh" in libc.
7. Exploit the buffer overflow this time to spawn a shell.

## Scripts used:
```
    See exploit.py
```
