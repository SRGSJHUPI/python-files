no_int,time_delay=map(int,input().split())
# list1=[]
cout=0
# for i in range(no_int):
     
#      inp=int(input())
     
#      list1.append(inp)

list1 = list(map(int, input().split()))

for i in range((no_int) -1):
     if (list1[-1-i]-list1[-2-i]<=time_delay and list1[-1-i]-list1[-2-i] >=0 ) or (list1[-2-i]-list1[-1-i]<=time_delay and list1[-2-i]-list1[-1-i] >=0) :
          cout=cout+1
     else:
          break     

print(cout +1)
# print("this is list1",list1)
