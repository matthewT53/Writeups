# Purchases:

## Binary Security:
* NX + Canary

## Challenges:
* The code addresses have a null byte in them. This is not a problem for fgets() however
the code after the call to fgets() presents a problem:
```asm
    lea rax, [rbp - 0x50]
    mov rdi, rax
    call strlen
    sub rax, 1
    mov byte [rbp - 0x50 + rax], 0
```
The code above will null parts of the address out. e.g 0x404040 (printf) becomes
0x00004040.

## Goal:
* Write the address of flag() directly to puts()'s GOT entry.

## Exploit notes:
* We put our %x and %$n before the address of puts to bypass the issue with strlen()
mentioned above.
* Using direct parameter access, we can write directly to the address of puts().
