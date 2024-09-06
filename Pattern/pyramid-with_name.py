num = int(input("Enter a number: "))
half = int(num//2)
name = input("Enter a name: ")
len = len(name)
name2 = ""
for i in range(0, len):
    name2 += name[i]+" "
for i in range(half+1):
    print(" "*(half-i) + "*  "*(i+1), end="")
    print("  "*(2*(half-i+1)) + "*  "*(i+1), end="")
    print("\n")
    # // for truncate division to give output int
if (num % 2 == 0):
    if (len % 2 == 0):
        print("*  "*((num-len)//2)+" ".join(name2)+"  *"*((num-len)//2))
    else:
        print("*  "*((num-len)//2)+" ".join(name2)+"  *"*((num-len)//2)+1)
    for i in range(num, 0, -1):
        print("  "*(num-i)+"*   "*(i), end="")
        print("\n")

else:
    if (len % 2 == 0):
        print("*  "*((num-len)//2)+" ".join(name2)+"  *"*((num-len)//2+1))
    else:
        print("*  "*((num-len)//2)+" ".join(name2)+"  *"*((num-len)//2))
    for i in range(num, 0, -1):
        print("  "*(num-i)+"*   "*(i-1), end="")
        print("\n")
