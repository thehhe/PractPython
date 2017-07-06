a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
sup = input("Give supremum: ")
for i in a:
    if i < int(sup):
        b.append(i)
        print(i)
print(b)
