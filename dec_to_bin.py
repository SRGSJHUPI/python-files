dec_no=int(input("please input decimal number:-"))
list1=[]
while not(dec_no==0 or dec_no==1):
   if dec_no%2==0:
      list1.append('0')
      dec_no/=2

   elif  dec_no%2==1:
      list1.append('1')
      dec_no=(dec_no-1)/2

list1.append('1')
list1.reverse()
string="".join(list1)


# for i in range(len(list1),0,-1):
  # print(list1[i-1])
print(string)
   




