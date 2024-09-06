sen=input("Enter a sentence: ")
i=sen.find("  ")
if (i>0):
    print("String contains double space!")
else:
    print("String don't contains double space!")

sen=sen.replace("  "," ")
print(sen)