#Server
import socket
s=socket.socket()
s.bind(("localhost",12345))
s.listen(3)
print("Socket is created & listening")
c,addr=s.accept()
print("Received Connection from",addr)
while True :
    data=input("Enter the message :")
    c.send(data.encode())
    if data=="close" :
        break
    msg=c.recv(1024).decode()
    print("Received message from client :",msg)
c.close()
s.close()




#Client 
import socket
s=socket.socket()
s.connect(("localhost",12345))
print("Successfyllt connected")
while True :
    msg=s.recv(1024).decode()
    if msg=="close" :
        break
    print("Received msg from server:",msg)
    s.send(msg.encode())
s.close()
