print("12 - 2 =", 8 + 2)

# Single Line Comment
"""Triple single quotes or double quotes for Multiline"""
"""Yo Yo"""

print("\nYeh Duniya\nYeh Dharti\nMere Kaam ki nhi\nAnjaam ki nhi")

# Backward slash for for including double quotes in a sentence
print('\nPingu "Harshu"')

# sep to define separator b/t each word and end to define how to end a sentence
print("Heya", 6, 9, sep="-", end="007\n")

a = 1  # stores 1 in memory and give its memory address to a, and whenever you print a you access 1 through it
b = float(2)
# print(1+2)
# print("1"+"2")

# Type Casting It can be achieved with the help of Python's built-in type
# conversion functions such as int(), float(), hex(), oct(), str(), etc.
x = "1"
y = "2"
print(x + y)
print(int(x) + int(y))

s1 = "\nEkansh"
s2 = "Jaiswal"
print(s1 + s2)

string = "100"
number = 70
string_number = int(string)
sum = number + string_number
print(sum)

# Implicit Typecasting

i = 5
print(type(i))
j = 7.4
print(type(j))
k = i + j
print(type(k))
print(k)
