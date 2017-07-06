def get_int(text="Please give a number: "):
    return int(input(text))


def get_fib(n):
    a = 1
    b = 1
    r = []
    if n == 0:
        return r
    elif n == 1:
        r.append(a)
        return r
    else:
        r.append(a)
        r.append(b)
        for i in range(0, n-2):
            if i % 2 == 0:
                b += a
                r.append(b)
            else:
                a += b
                r.append(a)
    return r

n = get_int()
fib = get_fib(n)
print(fib)