# Cookie Monster:

## Solution:
Parts of the flag are stored in the cookie called "flag" as a MD5 hash.
Whenever you make a get request to the website, a new flag is set depending
as a cookie depending on the previous flag.

Need to crack all the MD5 hashes to get the flag.

I used https://hashkiller.co.uk/Cracker/MD5 to crack the hashes.

## Scripts used:
See cookies.py.

## Flag:
pctf{c0oki3s_@re_yUm_bUt_tHEy_@ls0_r3vEAl_@_l0t}
