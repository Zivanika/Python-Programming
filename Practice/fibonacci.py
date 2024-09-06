def fibo_recur(num): #recursive
    if(num==0):
        # print(num)
        return 0
    elif(num==1):
        # print(num)
        return 1
    else:
        # print(num,end=" ")
        return fibo_recur(num-1) +fibo_recur(num-2)
    

def fibo_ite(num): #iterative
    print(0,1,end=" ")
    a=0
    b=1
    for i in range(num-1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")

print("Using recursive approach: ",fibo_recur(7))
print("Using iterative approach:")
fibo_ite(7)


def fibo_iterative2(n):
    prev=0
    curr=1
    for i in range(1,n):
        preprev=prev
        prev=curr
        curr=prev+preprev
    return curr

print("\nUsing another iterative method:",fibo_iterative2(7))