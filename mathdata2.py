que=input("")
length=len(que)
#count=0
y=length-1
#for i in range(y+1):
if que[y]=="?" :#or que[length-1]==" ":
        for i in range(y):
            if que[length-2]==" ":
               length=length-1
            else :   
                if que[length-2]=="a" or que[length-2]=="e" or que[length-2]=="i" or que[length-2]=="o" or que[length-2]=="u" or que[length-2]=="y" or que[length-2]=="A" or que[length-2]=="E" or que[length-2]=="I" or que[length-2]=="O" or que[length-2]=="U" or que[length-2]=="Y" :
                 print('YES')
                 break
                else :
                     print("NO") 
                     break;
      #  count=count+1
else:
        print("sorry it is not a question as it does not lasts with ?")
       
    
  

