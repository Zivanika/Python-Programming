a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) #False because list are mutable so they tend to change so has to be assigned to different memory locations
print(a == b) #True

# == compares value
# is compares reference or memory location

a=(1,2,3)
b=(1,2,3)

print(a is b) #True because constant, immutable values so dont waste another memory location instead assign it to same memory location as before
print(a == b) #True

a=6 
b=6
a is b #True because 6 is constant so immutable
a="Akshat"
b="Akshat"