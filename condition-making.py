balance = int(input("\nEnter your balance: "))
SpiderMan_Game_Disk = 3900
if (balance > SpiderMan_Game_Disk):
    print("\nYou have successfully bought the game !!".title())
    balance = balance-SpiderMan_Game_Disk
    print("\nAvailable Balance:", balance)
else:
    if (balance > 1000):
        print("\nMaybe you can try out other games..".title())
    elif (balance > 500) and (balance < 1000):
        print("You can purchase renewed games".title())
    else:
        print("You cannot buy the game. Insufficient funds".title())
