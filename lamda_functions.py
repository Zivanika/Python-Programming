# def cube(x):
#     return x * x * x

# print(cube(3))

square = lambda x: x * x
print(square(2))
cube = lambda x: x * x * x
print(cube(3))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))


def high(fx, value):
    return 6 + fx(value)


print(high(lambda x: x * x, 2))
