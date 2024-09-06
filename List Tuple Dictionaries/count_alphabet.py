list=['a','b','c','a','b','d','e','a','f','g','h']
count_a=0
count_b=0
count_c=0
for i in list:
    if (i=='a'):
        count_a+=1
    if (i=='b'):
        count_b+=1
    if (i=='c'):
        count_c+=1
print(f"The count of a in the list is {count_a}")
print(f"The count of b in the list is {count_b}")
print(f"The count of c in the list is {count_c}")