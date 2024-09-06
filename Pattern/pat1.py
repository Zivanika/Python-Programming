'''
*
**
***
****
*****
'''

for i in range(1, 6):
    for j in range(0, i):
        print("* ", end="")
    print("\n")

    '''
    *****
    ****
    ***
    **
    *
    '''
print("\nNEW PATTERN\n")
for i in range(5, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print("\n")

print("\nNEW PATTERN\n")

'''         *
           **
          ***
         ****
        *****   
'''
for i in range(1, 6):
    for j in range(5, i, -1):
        print("  ", end="")
    for k in range(i, 0, -1):
        print("* ", end="")
    print("\n")

# [Alternative] can also be used for equilateral triangle

for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ",end="")
    for k in range(1, i+1):
        print("*", end="")
    print("\n")

print("\nNEW PATTERN\n")
'''    *****
        ****
         ***
          **
           *   
'''
for i in range (1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(6-i,0,-1):
        print("*",end=" ")
    print("\n")
    
print("\n[NEW PATTERN]\n")
'''    *
      ***
     *****
    *******
   *********
'''
for i in range(1,6):
    for j in range(1,6-i):
        print("  ",end="")
    for k in range(0,2*i-1):
        print("* ",end="")
    print("\n")

print("\n[NEW PATTERN]\n")
'''  
   *********
    *******
     *****
      ***
       *
'''
for i in range(5,0,-1):
    for j in range(6-i,1,-1):
        print("  ",end="")
    for k in range(2*i-1,0,-1):
        print("* ",end="")
    print("\n")