n=int(input("Enter the value of n: "))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
print("\nIterative Way => ")
print("The sum of n Natural Numbers is",sum)

def Recur(num):
    if(num==1):
        return(1)
    else:
        return(num + Recur(num-1) )

print("\nRecursive Way => ")
print("The sum of n Natural Numbers is",Recur(n))
