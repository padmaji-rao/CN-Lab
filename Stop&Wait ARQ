#Sender Side
import socket
s=socket.socket()
host=socket.gethostname()
s.bind((host,9000))
s.listen(3)
timeout=5
isError=False
arr=[0,1]
i=0;
c,addr=s.accept()
print("Connection established with",addr)
while True:
    if not isError :
        sending_msg=input("Enter msg to send :")
        sending_msg=sending_msg+str(arr[i])
        print("Transmitting frame is :",sending_msg)
        x=sending_msg.encode()
        buff=x
        c.send(x)
        if i==0 :
            i=1  
        else :
            i=0
    else :
        c.send(buff)
        print("Re-transmitting frame is :",buff)
    try:
        c.settimeout(timeout)
        y=c.recv(1024).decode()
        print("Received Ack is :",y)
        isError=False
        pass
    except :
        print("------->Timed out<--------")
        isError=True
    
c.close()
s.close()




#Receiver Side
import socket
s=socket.socket()
host=socket.gethostname()
s.connect((host,9000))
arr=[0,1]
i=0
while True :
    recvd_msg=s.recv(1024).decode()
    print("Received msg :",recvd_msg)
    if recvd_msg[-1]==str(arr[i]) :
        if i==0 :
            i=1
        else :
            i=0
    else :
        print("Frame Duplication occurs")
    ack=input("Do you want to send ack?(y/n) :")
    if ack=="y" :
        ack=ack+str(arr[i])
        s.send(ack.encode())
        print("Sent Ack is :",ack)
    else :
        continue
s.close()
