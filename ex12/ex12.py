def get_first_and_last(l):
    r = []
    r.append(l[0])
    r.append(l[len(l)-1])
    return r

a = [i for i in range(5, 31, 5)]
print(a)
b = get_first_and_last(a)
print(b)