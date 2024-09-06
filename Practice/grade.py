print("Enter marks in 3 subjects: ")
m1=int(input())
m2=int(input())
m3=int(input())
total=(m1+m2+m3)/3
grade=""
if(total>90 and total<=100):
    grade="Ex"
elif(total>80 and total<=90):
    grade="A"
elif(total>70 and total<=80):
    grade="B"
elif(total>60 and total<=70):
    grade="C"
elif(total>50 and total<=60):
    grade="D"
elif(total>40 and total<=50):
    grade="E"
else:
    grade="F"
print(f"\nStudent has got {grade} Grade!!")