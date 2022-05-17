import random

def tossCoin():
    moves = ['head', 'tails']
    return "I am flipping the coin and i got " + random.choice(moves)
