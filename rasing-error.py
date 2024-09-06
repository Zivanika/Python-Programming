num = input("Enter a number b/t 4 & 7: ")
try:
    if (int(num) < 4) or (int(num) > 7):
        raise ValueError("Number not in the limits")
    elif (int(num) >= 4) or (int(num) <= 7):
        print("Numbers are correct!")

except:
    if num == "quit":
        pass
    else:
        raise TypeError("Alphabets not allowed")
print("Program Ended")

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...
