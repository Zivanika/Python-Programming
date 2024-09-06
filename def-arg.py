# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.


def func(a,b=2,c=10):
    print("Average: ",(a+b)/2)

func(10)

# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def func1(one,two,three):
    print("Colours => "+one,two,three)

func1(three="Blue",one="Green",two="Red")

# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

# Example 1: when number of arguments passed does not match to the actual function definition.

# def person(a_name,b_name,c_name):
#     print("Hello, "+a_name+b_name+c_name)

# person("Akshat ")

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
def Average(*values):
    sum=0
    for i in values:
        sum+=i
    print("Average is ",sum/len(values))

Average(1,2,3)

# Keyword Arbitrary Arguments:
# While creating a function, pass ** before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

def city(**cities):
    print(cities["US"],cities["India"],cities["NZ"])

city(US="New Youk",India="Allahabad",NZ="Auckland")
