wordlist = [line.strip() for line in open("wordlist.txt")]

for word in wordlist:
    if len(word) == 5:
        print(word[-1:-3: -1])
