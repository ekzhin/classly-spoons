#!/usr/bin/python
import socket

host = '192.168.0.1'
port = 25

foo = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

f1 = open('./emails.txt', 'r')
emails = f1.readlines()
f1.close()

foo = s.recv(512)
print foo
s.send('HELO foo\r\n')
foo = s.recv(512)
print foo

for email in emails:
    s.send('MAIL FROM: foo@sneakymailer.htb\r\n')
    foo = s.recv(512)
    print foo
    s.send('RCPT TO: ' + email)
    foo = s.recv(512)
    print foo
    s.send('DATA\r\n')
    foo = s.recv(512)
    print foo
    s.send('SUBJECT: foo\r\n')
    s.send('\r\nfoo\r\n.\r\n')
    foo = s.recv(512)
    print foo

s.send('QUIT\r\n')

s.close()
