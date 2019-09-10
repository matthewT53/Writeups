# Linux 1:

## Scenario:
* Basically there is a python script that opens a flag.txt and prints it.
* flag.txt has supposedly been deleted.
* The python script executed (still running) has a handle to it.

## Analysis:
* lsof is a tool that lists open files for a process.
* Running lsof:
```c
user@6d872420199b:~$ lsof -p 12
COMMAND PID USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
python   12 user  cwd    DIR  0,113     4096   517050 /home/user
python   12 user  rtd    DIR  0,113     4096  1290295 /
python   12 user  txt    REG  0,113  3492656   787017 /usr/bin/python2.7
python   12 user  mem    REG    8,1            787017 /usr/bin/python2.7 (path dev=0,113)
python   12 user  mem    REG    8,1            264588 /lib/x86_64-linux-gnu/libm-2.23.so (path dev=0,113)
python   12 user  mem    REG    8,1            264655 /lib/x86_64-linux-gnu/libz.so.1.2.8 (path dev=0,113)
python   12 user  mem    REG    8,1            264650 /lib/x86_64-linux-gnu/libutil-2.23.so (path dev=0,113)
python   12 user  mem    REG    8,1            264569 /lib/x86_64-linux-gnu/libdl-2.23.so (path dev=0,113)
python   12 user  mem    REG    8,1            264556 /lib/x86_64-linux-gnu/libc-2.23.so (path dev=0,113)
python   12 user  mem    REG    8,1            264624 /lib/x86_64-linux-gnu/libpthread-2.23.so (path dev=0,113)
python   12 user  mem    REG    8,1            264536 /lib/x86_64-linux-gnu/ld-2.23.so (path dev=0,113)
python   12 user    0r   CHR    1,3      0t0        6 /dev/null
python   12 user    1w  FIFO   0,12      0t0 14587656 pipe
python   12 user    2w  FIFO   0,12      0t0 14587657 pipe
python   12 user    3r   REG  0,113       37  1290334 /home/user/flag.txt (deleted)
```
We can see at the bottom, flag.txt has been deleted.
* Checking out /proc/<pid>/fd, we can see the file descriptor for flag.txt.
```c
user@6d872420199b:~$ ls -l /proc/12/fd
total 0
lr-x------ 1 user user 64 May  1 15:24 0 -> /dev/null
l-wx------ 1 user user 64 May  1 15:24 1 -> pipe:[14587656]
l-wx------ 1 user user 64 May  1 15:24 2 -> pipe:[14587657]
lr-x------ 1 user user 64 May  1 15:24 3 -> /home/user/flag.txt (deleted)
user@6d872420199b:~$ ls -l /proc/12/fd/3
lr-x------ 1 user user 64 May  1 15:24 /proc/12/fd/3 -> /home/user/flag.txt (deleted)
user@6d872420199b:~$ cp /proc/12/fd/3 flag.txt
user@6d872420199b:~$ cat flag.txt
CSACTF{f34r_cuts_d33p3r_th4n_sw0rds}
```
* We can simple copy the file back.

## Flag:
CSACTF{f34r_cuts_d33p3r_th4n_sw0rds}
