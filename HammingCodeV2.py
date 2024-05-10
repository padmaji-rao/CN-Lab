def get_no_of_p_bits(message) :
    for i in range(1,len(message)+2) :
        if 2**i >=len(message)+i+1 :
            return i
            
def get_hm_pattern(message,nopb) :
    tl=len(message)+nopb   
    message=message[::-1]           #<--    
    powers=[2**i for i in range(nopb)]  #<--
    pattern=[]
    for i in range(1,tl+1) :
        if i in powers :
            pattern.append("p")
        else :
            pattern.append(message[0])
            message=message[1:]       #<--
    return pattern[::-1]
    
def get_parity_bits(hm_pattern,nopb) :
    bins=[]
    for i in range(1,len(hm_pattern)+1) :
        b=bin(i)[2:]
        if len(b)<nopb :
            b="0"*(nopb-len(b))+b
        bins.append(b)        
    parity_bits=[]
    for i in range(1,nopb+1) :
        c=0
        for j in bins :
            if j[-i]=="1" :
                loc_in_hm=int(j,2)
                if hm_pattern[-loc_in_hm]=="1" :
                    c=c+1
        if c%2 ==0 :
            parity_bits.append("0")
        else :
            parity_bits.append("1")
    return parity_bits[::-1]     
    
def get_sending_message(message) :
    nopb=get_no_of_p_bits(message)
    print("No. of Parity Bits :",nopb)

    hm_pattern=get_hm_pattern(message,nopb)
    print("Hamming Pattern :",hm_pattern)

    parity_bits=get_parity_bits(hm_pattern,nopb)
    print("Parity Bits :",parity_bits)

    for i in hm_pattern :
        if i =="p" :
            loc=hm_pattern.index("p")
            hm_pattern[loc]=parity_bits[0]
            parity_bits=parity_bits[1:]
    return hm_pattern
    
def check_error(recvd_msg,nobp) :
    parity_bits=get_parity_bits(recvd_msg,nopb)
    parity_bits="".join(parity_bits)
    if parity_bits=="0"*nopb :
        print("No error")
    else :
        print("Error Detected at",int(parity_bits))
        
message=input("Enter message to send :")
nobp=get_no_of_p_bits(message)
sm=get_sending_message(message)
print(sm)

recvd_msg=list(input("Enter Received Message :"))
check_error(recvd_msg,nobp)
