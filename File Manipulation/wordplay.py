wordlist = [line.strip() for line in open("wordlist.txt")]

print("All three letter words")
for word in wordlist:
    if len(word) == 3:
        print(word)
