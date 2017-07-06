import random

def del_duplicates_sets(l):
    return list(set(l))


def del_duplicates_iter(l):
    r = []
    for i in l:
        if i not in r:
            r.append(i)
    return r

a = [random.randint(1, 10) for i in range(1, 10)]
print(a)

b = del_duplicates_iter(a)
c = del_duplicates_sets(a)
print(b)
print(c)
