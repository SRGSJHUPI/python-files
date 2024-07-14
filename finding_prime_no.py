inp=int(input("please enter the number:-"))
flag=True
if inp>2:
    for i in range(2,int(inp/2)+2):
        if inp%i==0:
            flag=False
            #print("not prime number")
            break

    # for i in range(2,int(inp/2)+2):
    #     if inp%i!=0:
    #         print("prime number")
    #         break    
        #elif inp%i!=0:
            # print("prime number")
            # break
#elif inp==2:
   # flag=True
    #print("prime number") 
# elif inp==1 :
#     print("not prime number")
# else :
#     flag=False
  #  print("not prime number") 
elif inp <=1:
    flag=False
elif inp==2:
    flag=True      
if flag:
    print("prime number")
else :
    print("not prime number")       
