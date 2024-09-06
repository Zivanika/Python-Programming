a=1
for i in range(6):
    for j in range(i):
        print(f"{a} ",end="")
        a+=1
    print("\n")
    
print("\n[NEW PATTERN]\n")
for i in range(5):
    val=i+1
    for j in range(i+1):
        print(f"{val} ",end="")
        val+=5-j-1       #num - 1, num -2, num -3 and so on
    print("\n")
    
print("\n[NEW PATTERN]\n")
for i in range(5):
    for j in range(i+1):
        x=0
        for k in range(j):
            x=x+5-k
        if(j%2==0):
            print(f"{x+i+1-j} ",end="")
        else:
            print(f"{x+5-i} ",end="")
    print("\n")

print("\n[NEW PATTERN]\n")
for i in range(4):
    for j in range(5-i):
        print("  ",end="")
    for j in range(i+1,0,-1):
        print(f"{j} ",end="")
    for j in range(2,i+2):
        print(f"{j} ",end="")
    print("\n")