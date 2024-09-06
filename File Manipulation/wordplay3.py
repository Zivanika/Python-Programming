wordlist = [line.strip() for line in open("wordlist.txt")]

for word in wordlist:
    if len(word) == 5 and word.startswith("ap") or word.endswith("le"):
        print(word)
