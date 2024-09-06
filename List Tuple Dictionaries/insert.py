list=[2,3,4,5,6]
num=int(input("Enter a number to insert at the beginning: "))
list.insert(0,num)
print(list)
num=int(input("Enter a number to insert at the end: "))
list.append(7)
print(list)
count=0
for i in list:
    count+=1
num=int(input("Enter a number to insert at the center: "))
list.insert(int(count/2),num)
print(list)
