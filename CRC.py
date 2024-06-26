def xor(msg1,msg2) :
    #print(msg1,msg2) #[msg1 is upper number and msg2 is lower number in normal division]
    res=bin(int(msg1,2)^int(msg2,2))[2:]
    if len(res)<len(msg2) : #checking for length of result is < divisor 
        res="0"*(len(msg2)-len(res)-1)+res
    return res
    
def get_remainder(dvnd,dvsr) :
    dvnd_length=len(dvnd)
    dvsr_length=len(dvsr)
    zeros="0"*dvsr_length  #used for dividing if MSB of temp_dividend is "0"
    temp_dvnd=dvnd
    for i in range(dvsr_length,dvnd_length+1) :
        if temp_dvnd[0]=="1" :
            rem=xor(temp_dvnd[:dvsr_length],dvsr)
        else :
            rem=xor(temp_dvnd,zeros)
        
        if i==dvnd_length :    #Incase we exclude this we get IndexError 
            pass
        else :
            temp_dvnd=rem+dvnd[i]
            #print(temp_dvnd) #[this is stepwise remainder after adding bit from dividend]
    print("Remainder :"+rem)
    return rem

def get_sending_message(sdw,gw) :
    temp=sdw
    temp=temp+((len(gw)-1)*"0")
    rem=get_remainder(temp,gw)
    return sdw+rem

sdw=input("Enter sending message (Data Word) :")  #sdw=sender_data_word
gw=input("Enter generator word :")  #gw=generator_Word
sm=get_sending_message(sdw,gw)  #sm=sending message
print("Sending Message (Coded Word) :"+sm)

rcw=input("Enter received message (Coded Word) :")  #received coded word
remainder=get_remainder(rcw,gw)

if remainder=="0"*(len(gw)-1) :
    print("No Error")
else :
    print("Error")
#print(get_remainder("100101100","1101"))
#print(get_remainder("110101100","1101"))



-----------------------------------Pure Code--------------------------------------------------------------------------------------------
def xor(msg1,msg2) :
    res=bin(int(msg1,2)^int(msg2,2))[2:]
    if len(res)<len(msg2) :
        res="0"*(len(msg2)-len(res)-1)+res
    return res
    
def get_remainder(dvnd,dvsr) :
    dvnd_length=len(dvnd)
    dvsr_length=len(dvsr)
    zeros="0"*dvsr_length
    temp_dvnd=dvnd
    for i in range(dvsr_length,dvnd_length+1) :
        if temp_dvnd[0]=="1" :
            rem=xor(temp_dvnd[:dvsr_length],dvsr)
        else :
            rem=xor(temp_dvnd,zeros)
        
        if i==dvnd_length :
            pass
        else :
            temp_dvnd=rem+dvnd[i]
    print("Remainder :"+rem)
    return rem

def get_sending_message(sdw,gw) :
    temp=sdw
    temp=temp+((len(gw)-1)*"0")
    rem=get_remainder(temp,gw)
    return sdw+rem

sdw=input("Enter sending message (Data Word) :")
gw=input("Enter generator word :")
sm=get_sending_message(sdw,gw)
print("Sending Message (Coded Word) :"+sm)

rcw=input("Enter received message (Coded Word) :")
remainder=get_remainder(rcw,gw)

if remainder=="0"*(len(gw)-1) :
    print("No Error")
else :
    print("Error")

