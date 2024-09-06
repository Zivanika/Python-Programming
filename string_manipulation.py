friend1="Akshat"
friend2='Harshita'
x='''love each other'''
print("They "+x) #Mind + only used in string concatenation and not like java to separate objects

# print(friend1[0])
# print(friend1[1])
# print(friend1[2])

#using len() function to calculate length
length=len(friend2)
print(length)

#string slicing
#count starts from index 0 and doesn't count last index
# print(friend1[0:3])
# print("or")
# print(friend1[:3])
# print(friend2[3:6])
# print(friend2[-2:8]) #means 2 minus len()
# print(friend1[-2:-6]) #means reverse printing
# print(friend1[-6:-2]) #means forward printing

nm="Harry"
# print(nm[-4:-2])

#String Functions

# Python provides a set of built-in methods that we can use to alter and modify the strings.


print(friend1.upper()) #Converts to uppercase
print(friend2.lower())  #Converts to lowercase
str1="Learning Python Coding"
print(str1.strip()) #The strip() method removes any white spaces before and after the string.

str2="!!!Helluuu!!!"
# print(str2.rstrip("!")) #the rstrip() removes any trailing characters.

print(str1.replace("Python","Java")) #The replace() method replaces all occurences of a string with another string.

print(str1.split(" ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items.

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())
 #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

str1 = "String Manipulation"
print(str1.center(50,"*"))   #The center() method aligns the string to the center as per the parameters given by the user.We can also provide padding character. It will fill the rest of the fill characters provided by the user. 
print("My Program".center(50,"*"))

str2="Mallayalum"
count=str2.count("l")
print("\nNumber of times l occured in \"Mallayalum\" is",count) #Can't use +count here cuz concatenation error


# print(str1.endswith("tion"))
# print(str1.startswith("Mani"))
# print(str2.endswith("lum",6,10))


index=str1.find("Money") #Calculates first index of M 
print("Index of Money: ",index)
#find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# index2=str1.index("Money")
# print(index2)

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

print(str1.isalnum())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False. Str1 gives false here because it contains white space

print(str1.isalpha())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# print(str2.islower())
# print(str2.isupper())

str3 = "We wish you a Merry Christmas"
print(str3.isprintable())
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.

newstr=str3.swapcase() #swaps lower with uppercase and vice versa
print(newstr)

print(str3.title())  #capitalise each word first letter
print(str3.istitle())