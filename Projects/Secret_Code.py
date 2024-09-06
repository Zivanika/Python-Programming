
import random
import string

msg = input("Enter a message: ")

if len(msg) <= 3:
    # Remove the first character using string slicing
    temp = msg[0]
    msg = msg[1:]
    msg += temp
    #list comprehension ''.join(listname) / listelement for i in range(3)
    random_chars = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(3))
    msg = random_chars+msg+random_chars
else:
    msg = msg[::-1]  # Reversing the string

print("Encrypted Message: ", msg)

ch = input("Do you want to decode the message? (Y/N): ")
if ch.lower() == "y":
    if len(msg) <= 3:
        msg = msg[::-1]  # Reversing the string
    else:
        msg = msg[3:-3]
        temp = msg[len(msg)-1]
        msg = temp+msg[:-1]
        
print("Decoded Message: ", msg)
