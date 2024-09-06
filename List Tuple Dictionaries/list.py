list = [1, 2, 3, "Ekansh", True]
print(len(list))

print(list[-3])  # list(5-3),list(2)
print(list[:])  # list[0:len(list)]
print(list[1:])
print(list[1:-1])  # 1 - 4, 4 doesn't count
print(list[0:5:2])

if "Ekansh" in list:
    print("Yes")
else:
    print("No")

if "Ek" in "Ekansh":
    print("Yes")
else:
    print("No")

animals = ["cat", "dog", "bat", "mouse", "lion", "tiger", "giraffe"]
print(animals[::2])
print(animals[-6:-1:2])

# List Comprehension
li = [i for i in range(4)]
print(li)
l2 = [i*i for i in range(10) if i % 2 == 0]
print(l2)

names = ["David", "Maria", "Lily", "Harry", "Micheal"]
l3 = [n for n in names if "a" in n]
print(l3)

l4 = [i for i in names if len(i) > 5]
print(l4)
