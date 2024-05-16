#Server---------------------------------------------------------------------
import socket
s=socket.socket()
s.bind(('localhost',55149))
s.listen(4)
z=0
c,addr=s.accept()
print("Conction estblshd with ",addr)
m=input("Enter data: ")
f=m.split()
print("Frames are ",f)
ws=int(input("Enter window size: "))
c.send(str(ws).encode())
k,j=0,0
while True:
    if z!=1:
        l=[]
        for i in range(ws):
            if i+j>=len(f):
                k=1
                break
            x=str(f[i+j])
            print("Transmitting msg:",x)
            l.append(x)
            c.send(x.encode())
        j+=ws
        buf=l
    else:
        for i in range(len(buf)):
            c.send(buf[i].encode())
            print("Retransmitting msg is:",buf[i])
    try:
        if k==1:
            break
        c.settimeout(12)
        rmsg=c.recv(1024).decode()
        print("Ack received is: ",rmsg)
        z=0
    except:
        if k==1:
            break
        print("Time out")
        z=1
c.close()
s.close()












#Client----------------------------------------------------------------------------------------------

import socket
s=socket.socket()
s.connect(('localhost',55149))
print("Connection established successfully")
ar=[]
ws=int(s.recv(1024).decode())
j=k=0
while True:
    for i in range(ws):
        x=s.recv(1024).decode()
        if len(x)==0:
            k+=1
            break
        print("Received msg is: ",x)
    if k==ws:
        break
    n=input("Either y/n? ")
    if n=='y':
        s.send(n.encode())
        print("ack sent is: ",n)
    else:
        continue     
s.close()
