list=[1,7,12,2,3]
print(list)
list.append(5)
print(list)

list.sort() #Asceniding
print(list)
list.sort(reverse=True) #Descending
print(list)

list.reverse() #do not print like this print(list.reverse())
print(list)

l=[1,3,5,1,6,7,1]
index=l.index(1)
print(index)
count=0

for i in range(0,len(l)):
    if l[i]==1:
        count+=1
    if count==3:
        print(l[i-1])

    
