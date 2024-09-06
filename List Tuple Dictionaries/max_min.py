tup=(2,6,8,2,1,5)
temp=list(tup)
temp.sort()
min=temp[0]
len=len(temp)
max=temp[len-1]
sum=0
for i in temp:
    sum+=i 
tup=tuple(temp)
# print(tup)
print(f"Minimum number is {min}")
print(f"Maximum number is {max}")
print(f"Average is {int(sum/len)}")
