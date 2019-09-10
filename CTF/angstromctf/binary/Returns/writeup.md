# Returns:

## Protections:
* NX stack

## Binary notes:
* Very similar to the challenge called "Purchases" except the buffer is now
50 bytes instead of 60 bytes.

## Challenges:
* There is no flag() function so we need to somehow call system with the argument
"/bin/sh".

## Exploit notes:
* We can use a tool called one_gadget to find an offset in libc that can call
do_system() which calls execve("/bin/sh", argp, env).
* The offset found is only 2.5 bytes e.g 0x45876 so we need to guess the last
three hex digits.
* Basically, this requires brute force.

## Steps to exploit:

## Scripts used:
```js
    See exploit.py
```
