# Aquarium:

## Protections enabled:
* NX stack

## Program description:
* There is a function called flag at 0x004011a6.

## Vulnerabilities:
* The function create_aquarium() calls gets() to receive the name of the fish.
* gets() is vulnerable to a buffer overflow attack.

## Exploit notes:
* Offset from start of buffer to ret address is 0xd8.

## Steps to exploit:

## Scripts used:
```js
    see exploit.py
```
