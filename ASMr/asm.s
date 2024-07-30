<main+0>:     main 
<main+4>:     push   rbp
<main+5>:     mov    rbp,rsp
<main+7>:     mov    rsi, 0x3F11E
<main+8>:     mov    DWORD PTR [rbp-0x4], 0xEBCE
<main+9>:     mov    DWORD PTR [rbp-0x5], 0x5383A
<main+10>:    mov    edi, DWORD PTR [rbp-0x5]
<main+11>:    mov    QWORD PTR [rbp-0x34], rsi
<main+17>:    cmp    edi, rsi
<main+18>:    jg     <main+29>
<main+20>:    imul   rsi, DWORD PTR [rbp-0x5]
<main+21>:    jmp    <main+29>
<main+22>:    mov    DWORD PTR [rbp-0x4], 0x53BD
<main+29>:    mov    eax, DWORD PTR [rbp-0x2]
<main+36>:    idiv   rsi, DWORD PTR [rbp-0x4]
<main+41>:    mov    eax, DWORD PTR [rbp-0x34]
<main+42>:    add    rsi, eax
<main+44>:    mov    eax, rsi
<main+44>:    imul   eax, 0x932
<main+47>:    mov    eax, eax
<main+47>:    pop    rbp
<main+48>:    ret


