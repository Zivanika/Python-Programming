x = 10  # global variable


def func():
    # x = 8  # local variable
    global x #global variable ko pakadlo
    x = 7
    y = 1
    # print(x)


print(x)
func()
# print(y) #Out of scope
print(x)
