num = input("Enter a number: ")

try:
    for i in range(1,11):
        print(f"{num} x {i} = {int(num)*i}")
    val = int(num) / 0
    list = [1, 2]
    print(list[5])
except ValueError:
    print("ERROR: Invalid Value entered")  # try blocks only executes one except block
except IndexError:
    print("ERROR: Index out of bounds")
except ZeroDivisionError:
    print("Divided by Zero")
except Exception as e:
    print("Some error happened")
    print(e)


print("Some IMP lines of code")
print("End of program")

# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
