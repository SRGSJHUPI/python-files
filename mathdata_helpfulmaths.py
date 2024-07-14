string=input("")
list3=[]
for i in string.split('+'):
    if i.isdigit():
        list3.append(i)
list3.sort()        
list1="+".join([str(a) for a in list3])
print(list1)

