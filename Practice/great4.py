print("Enter 4 numbers: ")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a>b):
    if(a>c):
        if(a>d):
            print("Largest Number is ",a)
        else:
            print("Largest Number is ",d)
    else:
        if(c>d):
            print("Largest Number is ",c)
        else:
            print("Largest Number is ",d)
else:
     if(b>c):
        if(b>d):
            print("Largest Number is ",b)
        else:
            print("Largest Number is ",d)
     else:
        if(c>d):
            print("Largest Number is ",c)
        else:
            print("Largest Number is ",d)