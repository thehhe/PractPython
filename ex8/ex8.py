while True:
    p1 = input("Pick out of r/p/s: ")
    p2 = input("Pick out of r/p/s: ")
    if p1 == "s":
        if p2 == "s":
            print("Draw\n")
        elif p2 == "r":
            print("Player 2 won!!\n")
        else:
            print("Player 1 won!!\n")
    elif p1 == "r":
        if p2 == "r":
            print("Draw\n")
        elif p2 == "p":
            print("Player 2 won!!\n")
        else:
            print("Player 1 won!!\n")
    else:
        if p2 == "p":
            print("Draw\n")
        elif p2 == "s":
            print("Player 2 won!!\n")
        else:
            print("Player 1 won!!\n")
    another = input("Do you want to play another game? (y/n): ")
    if another == "n":
        break
