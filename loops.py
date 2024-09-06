name = "Ekansh"
for i in name:
    print(i, end=" ")
    if(i=='h'):
        print(" J a i s w a l")

colors=["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
        
for i in range(5): #printing 1 to 5
    print(i+1)
    
print("\n")

for i in range(5 , 15): #for printing 5 to 14 (one less than upper bound)
    print(i)

for i in range(2,21,2): #one size greater because up is not counted
    print(i,end=" ") #because default end=\n

i=int(input("Enter a number: "))

while (i<=10):
    print(i)
    i=i+1
    
i=5
while(i>0):
    print(i)
    i=i-1
    

i=int(input("Enter a number: "))
while(i<=50):
    i=int(input("Enter a number: "))
print("Done.")

num=7
for i in range(12): 
    if ((i+1)==7):
        print("Skipped the iteration")
        continue
    if(i==10):
        break
    print("7 X ",i+1," = ",num*(i+1))

for i in [2,3,5,2,6,8,0,4]:
    if(i%2!=0):
         continue
    else:
        print(i)

number = 0
while number < 10:
    print(f"Number is {number}!")
    number = number + 1