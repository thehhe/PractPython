s = input("Please enter a word: ")
pal = True

for c in range(0, int(len(s)/2)):
    if s[c] != s[len(s)-c-1]:
        pal = False

print(pal)