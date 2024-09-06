def cube(x):
    return x * x * x


my_list = [2, 3, 4, 5, 6]
# I want to cube each item in list
# newl=[]
# for i in my_list:
#     newl.append(cube(i))
# print(newl)

# Map Function => map(function,iterable)
newl = list(map(cube, my_list))
print(newl)


def condition(a):
    return a > 3


# Filter Function => filter(preditate,iterable)
filterd = list(filter(condition, my_list))
print(filterd)


# Reduce(function,iterable) reduces an iterable to a single value by applying some logic on its elements

from functools import reduce

sum = reduce(lambda x, y: x + y, my_list)
print(sum)
