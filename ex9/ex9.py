import random

x = random.randint(1, 9)
i = 0

while True:
    g = input("Guess a number from 1 to 9: ")
    i += 1
    if int(g) > x:
        print("The number you put is too big. . .")
    elif int(g) < x:
        print("The number you put is too small. . .")
    else:
        print("You managed to find the hidden number (" + str(x) + ") after " + str(i) + " tries.")
        break