def xor(arg1,arg2) :
    rem=bin(int(arg1,2)^int(arg2,2))[2:]
    if len(rem) <len(arg2) :
        rem="0"*(len(arg2)-len(rem)-1)+rem
    return rem


def get_remainder(dvnd,dvsr) :
    dvndl=len(dvnd)
    dvsrl=len(dvsr)
    zeros="0"*len(dvsr)
    temp=dvnd
    for i in range(dvsrl,dvndl+1) :
        if temp[0]=="1" :
            rem=xor(temp[:dvsrl],dvsr)
        else :
            rem=xor(temp[:dvsrl],zeros)

        if i==dvndl :
            pass
        else :
            temp=rem+dvnd[i]
    return rem

def get_sending_msg(dw,gw) :
    temp=dw
    dw=dw+"0"*(len(gw)-1)
    rem=get_remainder(dw,gw)

    return temp+rem


dw=input("Enter data word :")
gw=input("Enter Generator word :")
cw=get_sending_msg(dw,gw)
print(cw)
recvd_msg=input("Enter the received msg :")
recvd_rem=get_remainder(recvd_msg,gw)
if recvd_rem=="0"*(len(gw)-1) :
    print("No Error")
else :
    print("Error Occurred")
