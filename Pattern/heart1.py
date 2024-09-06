# for i in range(6):
#     for j in range(7):
#         if(j%3==0):
#             print("   ",end="")
#         else:
#             print("*  ",end="")
#     break
# print("\n")
# for i in range(5):
#     for k in range(6):
#         if(k%3==0):
#             print("*  ",end="")
#         else:
#             print("   ",end="")
#     break
# for i in range(4):
#     for j in range(6):
#         if(i==j) or (i+j==6):
#             print("*  ",end="")
#         else:
#             print("   ",end="")
#     print("\n")

for i in range(6):
    for j in range(7):
        if(i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*  ",end="")
        else:
            print("   ",end="")
    print("\n")
