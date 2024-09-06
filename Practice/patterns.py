for i in range(1, 4):
    for j in range(4-i):
        print("  ", end="")
    for j in range((2*i)-1):
        print("* ", end="")
    print("\n")
print("\n[NEW PATTERN]\n")
for i in range(3):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
print("\n[NEW PATTERN]\n")
for i in range(3):
    for j in range(3):
        if (i == j == 1):
            print("   ", end="")
        else:
            print("*  ", end="")
    print("\n")
    
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*  ",end="")
        print("\n")
print("\n[NEW PATTERN]\n")
pattern(3)