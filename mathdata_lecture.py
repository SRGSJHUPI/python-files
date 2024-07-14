nola,no_word=map(int,input().split())
index=0
list1,list2,list4=[],[],[]
for i in range(no_word):

    inpt1=input().split()
    inp1=list(inpt1)
    list1.append(inp1[0])
    list2.append(inp1[1])

inp22=input().split()
list3=list(inp22)

for i in range(nola):
    for j in range(no_word):
        if list3[i]==list1[j]:
            index=j
            if len(list3[i])<=len(list2[j]):
                list4.append(list3[i])
            else:
                list4.append(list2[j])

print(*list4)


    # inpt2=input().split()
    # inp2=list(inpt2)

    # inpt3=input().split()
    # inp3=list(inpt3)
  