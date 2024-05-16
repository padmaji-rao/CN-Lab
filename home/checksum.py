def get_checksum(msg,fs) :
    fl=[]
    while len(msg)>0 :
        if len(msg)>fs :
            item=msg[:fs]
            fl.append(item)
        else :
            item="0"*(fs-len(msg))+msg
            fl.append(item)
        msg=msg[fs:]

    print(fl)

    total="0"
    for i in fl :
        total=bin(int(total,2)+int(i,2))[2:]
        if len(total)>fs :
            total=bin(int(total[1:],2)+int("1",2))[2:]
        if len(total)<fs :
            total="0"*(fs-len(total))+total
    checksum=""
    for i in total :
        if i=="1" :
            checksum=checksum+"0"
        else :
            checksum=checksum+"1"

    return checksum


msg=input("Enter the input message :")
fs=int(input("Enter the frame size :"))
scs=get_checksum(msg,fs)
print("Checksum :",scs)
sm=msg+scs
print("Sending Message:",sm)

recvd_msg=input("Enter received msg :")
recvd_cs=recvd_msg[-fs:]
recvr_cs=get_checksum(recvd_msg[:-fs],fs)

if recvr_cs==recvd_cs :
    print("No Error")
else :
    print("Error Occurred")
