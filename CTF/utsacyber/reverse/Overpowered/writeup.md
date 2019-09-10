# Overpowered:

## What we have:
* We are provided with a string of hexadecimal numbers like so:
```c
31c0c745b019091b19c745b40e1c2123c745b86a2f0531c745bc346a2d05c745c0373b3932c745c
46b343f05c745c8363b343dc745cc2f3b3d6966c745d02700c745ac00000000eb1e8d55b08b45ac
01d00fb60083f05a89c18d55d28b45ac01d088088345ac0183ec0c8d45b050e8fafdffff83c4108
9c28b45ac39c277ca
```

## Analysis:
* The hexadecimals above decompile to:

```C
0:  31 c0                   xor    eax,eax
2:  c7 45 b0 19 09 1b 19    mov    DWORD PTR [ebp-0x50],0x191b0919
9:  c7 45 b4 0e 1c 21 23    mov    DWORD PTR [ebp-0x4c],0x23211c0e
10: c7 45 b8 6a 2f 05 31    mov    DWORD PTR [ebp-0x48],0x31052f6a
17: c7 45 bc 34 6a 2d 05    mov    DWORD PTR [ebp-0x44],0x52d6a34
1e: c7 45 c0 37 3b 39 32    mov    DWORD PTR [ebp-0x40],0x32393b37
25: c7 45 c4 6b 34 3f 05    mov    DWORD PTR [ebp-0x3c],0x53f346b
2c: c7 45 c8 36 3b 34 3d    mov    DWORD PTR [ebp-0x38],0x3d343b36
33: c7 45 cc 2f 3b 3d 69    mov    DWORD PTR [ebp-0x34],0x693d3b2f
3a: 66 c7 45 d0 27 00       mov    WORD PTR [ebp-0x30],0x27
40: c7 45 ac 00 00 00 00    mov    DWORD PTR [ebp-0x54],0x0
47: eb 1e                   jmp    0x67
49: 8d 55 b0                lea    edx,[ebp-0x50]
4c: 8b 45 ac                mov    eax,DWORD PTR [ebp-0x54]
4f: 01 d0                   add    eax,edx
51: 0f b6 00                movzx  eax,BYTE PTR [eax]
54: 83 f0 5a                xor    eax,0x5a
57: 89 c1                   mov    ecx,eax
59: 8d 55 d2                lea    edx,[ebp-0x2e]
5c: 8b 45 ac                mov    eax,DWORD PTR [ebp-0x54]
5f: 01 d0                   add    eax,edx
61: 88 08                   mov    BYTE PTR [eax],cl
63: 83 45 ac 01             add    DWORD PTR [ebp-0x54],0x1
67: 83 ec 0c                sub    esp,0xc
6a: 8d 45 b0                lea    eax,[ebp-0x50]
6d: 50                      push   eax
6e: e8 fa fd ff ff          call   0xfffffe6d
73: 83 c4 10                add    esp,0x10
76: 89 c2                   mov    edx,eax
78: 8b 45 ac                mov    eax,DWORD PTR [ebp-0x54]
7b: 39 c2                   cmp    edx,eax
7d: 77 ca                   ja     0x49
```
Thanks: https://defuse.ca/online-x86-assembler.htm#disassembly2

## Solution:
* XOR decode the byte string from (EBP - 0x50) to (EBP - 0x30) using the key
0x5a.

## Scripts used:
* See solve.py

## Flag:
CSACTF{y0u_kn0w_mach1ne_languag3}
