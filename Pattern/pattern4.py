str1 = " * "
print(str1*5)
for i in range(8):
    print(str1.center(15))
print(str1*5)
print("\n")

for i in range(2, 4):
    print((" * "*i).center(10), (" * "*(i)))

for i in range(7, 0, -1):
    print((str1*i).center(20), "\n")

for i in range(7):
    print(("*          *").center(10))
print("*"*12)
