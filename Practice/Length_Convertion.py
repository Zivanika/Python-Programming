def Converter1():
    inch = float(input("Enter Inches: "))
    cm = inch*2.54
    print("Centimeters:", cm)


def Converter2():
    cm = float(input("Enter Centimeters: "))
    inch = cm*0.393701
    print("Inches:", inch)


print("which unit to convert?".title())
print(" 1. Inches => Centimeters")
print(" 2. Centimeters => Inches")
ch = int(input("Enter your choice: "))
match ch:
    case 1:
        Converter1()
    case 2:
        Converter2()
    case _:
        print("Wrong Choice!")
