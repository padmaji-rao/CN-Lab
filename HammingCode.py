#Following comments are considering this message="10"
def get_no_of_p_bits(m) :
    for i in range(1,len(m)+2) :
        if 2**i >=len(m)+i+1 :
            return i

def get_parity_indexes(tl,nopb) :
    bins=[]         #bins[] used to store binary values from 1 to totalLength
    for i in range(1,tl+1) :
        b=bin(i)[2:]
        if len(b)<nopb :
            b="0"*(nopb-len(b))+b
        bins.append(b)     
                        #bins=['001', '010', '011', '100', '101']
    p_indexes=[]                              
    for i in range(1,nopb+1) :
        l=[]
        for j in bins :
            if j[-i]=="1" :
                l.append(int(j,2))
        p_indexes.append(l)
    return p_indexes           #[[1, 3, 5], [2, 3], [4, 5]]           
    
def get_parity_bits(hm,p_indexes) :  
    l=[]
    for i in p_indexes :
        c=0
        for j in i :
            if hm[-j]=="1" :
                c=c+1
        if c%2==0 :
            l.append("0")
        else :
            l.append("1")
    return l[::-1]                     #['0', '1', '0', '0']
                
def get_hm(msg,tl) :
    hm=[]
    pl=[]    #parity_locations
    msg=msg[::-1]    #msg="01"
    for i in range(tl-len(msg)) :
        pl.append(2**i)
    #After loop : pl=[1, 2, 4]
    for i in range(1,tl+1) :
        if i in pl :
            hm.append("p")     #Placing "p" at parity locations
        else :
            hm.append(msg[0])
            msg=msg[1:]
    hm=hm[::-1]          #Before reversing : hm=['p', 'p', '0', 'p', '1']
    return hm            #After reversing : hm['1', 'p', '0', 'p', 'p']
                
def get_sending_message(msg,nopb) :
    tl=len(msg)+nopb   #tl=5
    hm=get_hm(msg,tl)   #['1', 'p', '0', 'p', 'p']
    p_indexes=get_parity_indexes(tl,nopb)   #[[1, 3, 5], [2, 3], [4, 5]]
    pb=get_parity_bits(hm,p_indexes)    #['1', '0', '1']
    for i in range(nopb):
        loc=hm.index("p")
        hm[loc]=pb[0]
        pb=pb[1:]
    return "".join(hm)      #11001
           
def checking_error(msg,nopb) :
    p_indexes=get_parity_indexes(len(msg),nopb)  #[[1, 3, 5], [2, 3], [4, 5]]
    p_bits=get_parity_bits(list(msg),p_indexes)  
    p_bits="".join(p_bits)
    if p_bits=="0"*nopb :
        print("No error Detected in the message")
    else :
        loc=int(p_bits,2)
        print("Error Detected at location (from left) :",loc)
        msg_list=list(msg)
        if msg_list[-loc]=="0" :
            msg_list[-loc]="1"
        else :
            msg_list[-loc]="0"
        corrected_msg="".join(msg_list)
        print("Corrected Message :",corrected_msg)
        
message=input("Enter message to send :")
nopb=get_no_of_p_bits(message)
print("No. of Parity bits :",nopb)
transmitted_msg=get_sending_message(message,nopb)
print("Transmitted Message :",transmitted_msg)

received_msg=input("Enter received msg :")
checking_error(received_msg,nopb)
