wordlist = [line.strip() for line in open("wordlist.txt")]

for word in wordlist:
    if word.startswith("ca") or word.startswith("ba"):
        print(word)
