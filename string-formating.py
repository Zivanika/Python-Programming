sentence="Hello, My name is {1} and I live in {0}"
print(sentence)
name="Akshat"
country="India"
sentence.format(name,country)
sentence=f"Hello, My name is {name} and I live in {country}"
print(sentence)

price=49.2156
print(f"The MRP of the game: {price:.2f}")  #takes only 2 decimal place

print(f"Whats 2 x 7?\n{2*7}")

print(f"The addition of 2+5 using f-string can be done as {{2+5}}\n{2+5}") #If you want to show the f-string