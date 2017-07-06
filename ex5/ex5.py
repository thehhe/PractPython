a = range(2, 30, 2)
b = range(1, 20)

c = []

for i in a:
    if i in b:
        if i not in c:
            c.append(i)

print(c)