def C_F():
    temp = int(input("\nCelsius: "))
    new_temp = temp*1.8 + 32
    print("Fahrenheit:", new_temp)


def F_C():
    temp = int(input("\nFahrenheit: "))
    new_temp = (temp-32)*0.556
    print("Celsius:", new_temp)


print("which unit to convert?".title())
print(" 1. Celsius => Fahrenheit")
print(" 2. Fahrenheit => Celsius")
ch = int(input("Enter your choice: "))
match ch:
    case 1:
        C_F()
    case 2:
        F_C()
    case _:
        print("Wrong Choice!")
