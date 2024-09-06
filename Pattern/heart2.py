for i in range (6):
    for j in range(7):
        if(i==0 and j%3!=0):
            print("*  ",end="")
        else:
            print("   ",end="")
    print("\n")
    break
print("*  "*(7)+"\n")
for i in range(4,0,-1):
    for j in range(4-i):
        print("   ",end="")
    for j in range(2*(i)-1):
        print("*  ",end="")
    print("\n")
