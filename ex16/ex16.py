import string, random
lowerCaseLetters = list(string.ascii_lowercase)
upperCaseLetters = list(string.ascii_uppercase)


def generate_passwd(n=8):
    passwd = []
    for i in range(0, n):
        x = random.randint(1, 3)
        if x == 1:
            passwd.append(lowerCaseLetters[random.randint(0, len(lowerCaseLetters)-1)])
        elif x == 2:
            passwd.append(upperCaseLetters[random.randint(0, len(upperCaseLetters)-1)])
        else:
            passwd.append(str(random.randint(0, 9)))
    return passwd

a = input("Give length of a password (default 8): ")
passwd = generate_passwd(int(a))
print("".join(passwd))
