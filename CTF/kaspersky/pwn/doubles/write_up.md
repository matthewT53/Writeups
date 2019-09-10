# doubles:

## Challenges:
* ASLR + NX is turned on.

## Program notes:
* The program allocates a page of memory that is RWX.
* The program will take as input a maximum of 6 doubles which is basically
6x8 = 48 bytes.
* The double values are stored at the beginning of the page that is allocated.
* The program then jumps to this page at an offset of 0x78 bytes.

## Goals:
1. Construct 64 bit shellcode that can spawn a shell.
2. Convert the bytes of this shellcode into doubles.
3. Determine the final double number to send in to produce a jump instruction.

```js
    xmm1 = Sum of the double numbers.
    xmm0 = 6

    xmm1 / xmm0 is stored at [page + 0x78].  
```

## Shellcode details:
* The shellcode that spawns a shell will first set RSP to point to
the midpoint of the GOT section.
* The shellcode that will jump to the first shellcode is a simple
```js
    eb 86   jmp -0x78
```
* Need to create a sum that when divided by the number of doubles produces the
last two byte as 0x8eeb

## Constraints:
* Our shellcode must be less than 48 bytes.

## Steps to exploit:
1. Convert the shell spawning shellcode to groups of 8 bytes that can be used as doubles.
   For each of the 8 bytes, run p/f in GDB to find the double value that the bytes
   represent. Check that the double values correctly represent the shellcode by
   examining the allocated page.
2. The last part of the shellcode is only 4 bytes so it needs to be padded with 4
   0x90's (nops).
3. Determine in hex the value of the 5th double value to send into the program.
   Run the C program that comes with this exploit kit and run p/f in GDB on
   the value reported by "Next double".
4. Send the 5 double values into the program and shell should appear.

## Scripts used:
```js
    Go and look in exploit.py and find_double.c
```

## Flag:
KLCTF{h4ck1ng_w1th_d0ubl3s_1s_n0t_7ha7_t0ugh}
