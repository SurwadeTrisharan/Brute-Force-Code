# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 18:39:08 2024

@author: mr.jaadugar
"""
import socket, time

a=[]
t0=time.time()
with open("D:\\Hacking\\wordlist-master\\wordlist-master\\usernames.txt", "r") as f:
    for line in f:
        a.append(line.rstrip('\n'))
f.close()
n=len(a)

for i in range(0, n, 100):
    s = socket.socket()
    s.connect(("10.10.48.1", 80))
    for j in range(0, 100):
        k = i + j
        if k < n:
            req = "HEAD /" + a[k] + " HTTP/1.1\r\nHost: hackazon.samsclass.info\r\n\r\n"
            s.send(req.encode())         # Encode the request to bytes
            r = s.recv(8192)[9:12]
            if r != b"404":              # Compare with byte string
                print(a[k], r.decode())  # Decode the response for printing
    s.shutdown(socket.SHUT_WR)
    s.close()

print("Guesses: ", n, " Elapsed time: ", time.time() - t0, " sec.")
