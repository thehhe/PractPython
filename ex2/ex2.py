nr = input("Give a number: ")

if int(nr) % 2 == 0:
    if int(nr) % 4 == 0:
        print("Your number is dividable by 4")
    else:
        print("Your number is dividable by 2 and not by 4")
else:
    print("Your number is odd")

