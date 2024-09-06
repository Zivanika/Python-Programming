msg='Hello World'
for i in range(len(msg)):
    ind=97
    for j in range(26):
        print(chr(ind+j),end="\n")
    print(msg[:i+1])
    # print(msg)
        