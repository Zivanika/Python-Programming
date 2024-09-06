def Func(word,lt):
    lt.remove(word)
    return(lt)

l=["Apple","Banana","Strawberry","Orange","Mango"]
print(l)
word=input("\nEnter the fruit you don't like, we will remove it :\n")
word.capitalize()
l=Func(word,l)
print("\nNew List => ",l,"\nSee?")