print("Enter marks in 3 subjects: ")
m1=int(input())
m2=int(input())
m3=int(input())
total=(m1+m2+m3)/3
flag=1
if(total>=40):
    if(m1>=33 and m2>=33 and m3>=33):
        pass
    else:
        flag=0
else:
    flag=0
    
if(flag==1):
    print("Student has Passed!!")
else:
    print("Student has Failed!!")