n=int(input("please enter no of elements in array:- "))
arr=[]
for i in range(n):
  inp=  int(input("plese enter " + str(i+1) + "th element:- "))
  arr.append(inp)

for i in range(n-1):
    for p in range(n-1-i):
      if arr[p]>arr[p+1]:
         temp=arr[p+1]
         arr[p+1]=arr[p]
         arr[p]=temp

print(arr)


