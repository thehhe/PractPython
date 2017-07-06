from math import sqrt

a = input("Give a number: ")
divs = []
for i in range(2, int(sqrt(int(a)))+1):
    if int(a) % i == 0:
        divs.append(i)
        divs.append(int(int(a) / i))
divs.sort()
print(divs)