s = input("Please give a sentence: ")
c = s.split()

# for i in range(len(c)-1, -1, -1):
#     print(c[i])
c1 = [c[i] for i in range(len(c)-1, -1, -1)]
s = " ".join(c1)
print(s)