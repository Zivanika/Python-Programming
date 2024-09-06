words={"sabd":"word","pita":"father","mata":"mother","behan":"sister","bhai":"Brother","khel":"game","kehlona":"toy","aankh":"eye","kaan":"ear","naak":"nose"}
s=input("Enter a Hindi word you want the English Translation of >>> ")
if words.get(s)==None:
    print("Sorry, we need to update our dictionary!")
else:
    print(words.get(s))