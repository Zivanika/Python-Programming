# print("Enter Time (24 Hours Format):")
# hr=int(input("Hour: "))
# min=int(input("Minutes: "))
# timestamp = time.strftime('%H:%M:%S')

import time
hr = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))
name=time.strftime("%A")
print(name)
print("Time:",hr,":",min,":",sec)
if (hr >= 0) and (hr < 5):
    print("\nGood Night!")
elif (hr > 5) and (hr < 12):
    print("\nGood Morning!")
elif (hr >= 12) and (hr < 17):
    print("\nGood Afternoon!")
else:
    print("\nGood Evening!")
    

# https://docs.python.org/3/library/time.html#time.strftime
    

