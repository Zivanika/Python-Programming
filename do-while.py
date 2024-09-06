count = 1
secret_pwd = "Valar Dohaeris"
while True:
    pwd = input("Enter Password: ")
    if pwd == secret_pwd:
        break
    if (pwd != secret_pwd) and (count > 2):
        print("You Are Locked!")
        break
    print("Invalid!")
    count = count + 1
