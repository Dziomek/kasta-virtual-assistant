from random import randint


def generateToken():
    token = ''
    for i in range(6):
        token += str(randint(0, 9))
    return token
