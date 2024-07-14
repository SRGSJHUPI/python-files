str1=input("")
str2=input("")
len1=len(str1)
len2=len(str2)
cout=0
for i in range(min(len1,len2)):
    if(str1[-1-i]==str2[-1-i]):
        cout+=1
    else :
        break

print(len1+len2-2*cout)


    