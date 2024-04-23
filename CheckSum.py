def find_checkSum(sender_message,n):
                                                                    ##Dividing the message into frames
    frames_list=[]
    while len(sender_message)>0 :
                                            #if the frame contains less number of bits than frame size
        if(len(sender_message)<n):             
            frames_list.append((n-len(sender_message))*"0"+"".join(sender_message))
                                            
        else :                              #if frame satisfies frame size    
            frames_list.append("".join(sender_message[:n]))
            
        sender_message=sender_message[n:]
                                                                
                                                                    ##Calculating the sum of frames
    totalSum="0"
    for i in frames_list :
        totalSum =bin(int(totalSum,2)+int(i,2))[2:]          #Binary addition
        
        if(len(totalSum)>n):                #if the temporary sum contains CARRY BIT
            totalSum=bin(int(totalSum[1:],2)+int("1",2))[2:]
            
            if(len(totalSum)<n) :           #if the totalSum contains less number of bits than frame size
                totalSum=(n-len(totalSum))*"0"+totalSum
        
    checkSum=""                 
    for i in totalSum:
        if i=="0" :
            checkSum=checkSum+"1"
        else :
            checkSum=checkSum+"0"
    return checkSum
    
    
sender_message=list(input("Enter message to send :"))
n=int(input("Enter frame size :"))

SenderCheckSum=find_checkSum(sender_message,n)
SenderMessageWithChecksum="".join(sender_message)+SenderCheckSum
print("Sender Checksum :"+SenderCheckSum)
print("Sending Message :"+SenderMessageWithChecksum)

receiver_message=list(input("Enter received message with checksum :"))
ReceivedCheckSum="".join(receiver_message[-n:])
ReceiverCheckSum=find_checkSum(receiver_message[:-n],n)
print("Receiver Checksum :"+ReceiverCheckSum)

if(ReceivedCheckSum==ReceiverCheckSum) :
    print("Received Correct Message")
else :
    print("Received Wrong Message")
