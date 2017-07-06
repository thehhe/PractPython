from math import sqrt


def get_int(text = "Please give a number: "):
    return int(input(text))


def is_divisor(a, b):
    if b % a == 0:
        return True
    else:
        return False


def is_prime(n):
    if n <= 2:
        return False
    else:
        for i in range(2, int(float(sqrt(n))+1)):
            if is_divisor(i, n):
                return False
        return True

n = get_int()
print(is_prime(n))