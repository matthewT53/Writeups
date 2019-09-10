# Monkey:

## Analysis:
* USB traffic capture.

## Solution:
* Some characters are doubled so just try to formulate the correct word despite
these discrepancies.
* The analyze.py script produces:
CSCSSACTF{the_inffiinitete_monkeeyy_theorerem}<<<<[DEL]0<<<<<<<<<[DEL]0<<<<<[DEL]1<<[DEL]1<<<[DEL]1
* After formulating the correct words:
CSACTF{the_infinite_monkey_theorem}
* Looking at the < and the [DEL] as well as the numbers, it is obvious that
the 0 replaces the o in monkey and theorem. The 1 replaces the i's in infinite.

## Flag:
CSACTF{the_1nf1n1te_m0nkey_the0rem}
