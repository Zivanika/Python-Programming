while(True):
    name=input("Enter Username: ")
    if(len(name)>10):
        print("Valid Username!!")
        break
    else:
        print("Not Valid. Please try again.")