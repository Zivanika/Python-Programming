def Buzz(num):
    if (num % 7 == 0) or (num % 10 == 7):
        print("Number is a Buzz Number.")
        return num
    else:
        print("Number is NOT a Buzz Number")
        return num

a = int(input("Enter a number: "))
Buzz(a)

def Func1():
    pass
