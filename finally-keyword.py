try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
# finally:
#     print("This block is always executed.")
print("This block is always executed") #can go both ways in normal control

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
#finally will get executed even if the function has returned a value

# it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.