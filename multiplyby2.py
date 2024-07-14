inp =int(input())
for i in range(inp):
    inp2=int(input())
    cout=0
    cout2=0
    for i in range(inp2):
     if inp2%3==0:
            cout=cout+1 
            inp2=inp2/3
     elif inp2%2==0:
            cout2=cout2+1
            inp2=inp2/2
     elif inp2==1:
            if cout>=cout2:
                print(cout-cout2+cout)
                break
            else:
                print(-1)
                break
     elif inp2%3!=0 or inp2%2!=0:
            cout=-1
            cout2=0
            print(-1)
            break

# inp=int(input(""))
# list1=[]
# ii=0
# cout=0
# for i in range(inp):
#     inp2=int(input(""))
#     list1.append(inp2)
# while(inp2[ii]%6!=0):
#      inp2[ii]/6
#      cout=cout+1
     
# for i in range(list1[i]):
#         if list1[i]%3==0:
#             ii=ii+1 
#             list1[i]=list1[i]/3
#         elif list1[i]%2==0:
#             cout=cout+1
#             list1[i]=list1[i]/2
#         elif list1[i]==1:
#             if ii>=cout:
#                 print(ii-cout+ii)
#                 break
#             else:
#                 print(-1)
#                 break
#         elif list1[i]%3!=0 or list1[i]%2!=0:
#             ii=-1
#             cout=0
#             print(-1)
#             break