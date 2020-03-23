# Python Script I made to generate passwords.

def str(num): #num refers to the length you want your password to be.
    import string, random
    password = []
    for i in range(0, num):
        y = random.randint(0, 85) # This could be changed to include more characters.
        password.append(string.printable[y])
    passwordfinal = "".join(password)
    return print(passwordfinal)
