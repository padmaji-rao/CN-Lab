#Sender------------------------------------------------------------------------------
import socket
s=socket.socket()
s.bind(("localhost",13333))
s.listen(3)
print("Socket is Created and Listening")
timeout=10
z=0
cli,addr=s.accept()
while True :
    if z!=1 :
        msg=input("Enter msg to send :")
        cli.send(msg.encode())
        if msg=="close" :
            break
    else :
        print("Retransmitting-------->Frame:",msg)
        cli.send(msg.encode())
    try :
        cli.settimeout(timeout)
        ack=cli.recv(1024).decode()
        print("Received Ack :",ack)
        z=0
    except :
        print("---->TIMEOUT<-----")
        z=1
cli.close()
s.close()







#Client---------------------------------------------------------------------------------

import socket
s=socket.socket()
s.connect(("localhost",13333))
print("Client is Created and Connected")
while True :
    msg=s.recv(1024).decode()
    if msg=="close":
        break
    print('Received Msg :',msg)
    ack=input("Do you want to send ack (y/n)?")
    if ack=="y" :
        s.send(ack.encode())
        print("Sent Ack :",ack)
    else :
        continue
s.close()
