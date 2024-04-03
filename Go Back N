#Sender
import socket
s=socket.socket()
s.bind(('localhost',9000))
s.listen(3)
z=0

c,addr=s.accept()
print("Connection established with",addr)
m=input("Enter msg:")
arr=m.split()
print("Window is:",arr)
ws=int(input("Enter window size:"))
c.send(str(ws).encode())
k=0
j=0
while True:
    if z!=1:
        l=[]
        for i in range(ws):
            if i+j>=len(arr):
                k=1
                break
            x=str(arr[i+j])
            print("Transmitting frame :",x)
            l.append(x)
            c.send(x.encode())
        j+=ws
        buf=l
    else:
        for i in range(len(buf)):
            c.send(buf[i].encode())
            print("Retransmitting frame :",buf[i])
    try:
        if k==1:
            break
        c.settimeout(10)
        y=c.recv(1024).decode()
        print("Ack received:",y)
        z=0
        pass
    except:
        if k==1:
            break
        print("Timer Times out")
        z=1
c.close()
s.close()


#Receiver
import socket
s=socket.socket()
s.connect(('localhost',9000))
arr=[]
ws=int(s.recv(1024).decode())
j=0
k=0
while True:
    for i in range(ws):
        x=s.recv(1024).decode()
        if len(x)==0:
            k=1
            break
        print("Received msg :",x)
    if k==1:
        break
    n=input("Do you want to send Ack?(y/n):")
    if n=='y':
        s.send(n.encode())
        print("ACK sent :",(n))
    else:
        continue
s.close()
