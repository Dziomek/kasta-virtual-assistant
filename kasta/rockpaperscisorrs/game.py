import random


def game(player_move):
    moves = ["paper", "rock", "scisorrs"]
    computer_move = random.choice(moves)
    print((computer_move))
    print((player_move))
    player_move = player_move.strip()


    if player_move == computer_move:
        return (f"Both players selected {player_move}. It's a tie!")
    elif player_move in "rock":
        if computer_move == "scissors":
            return ("Rock smashes scissors! You win!")
        else:
            return("Paper covers rock! You lose.")
    elif player_move == "paper":
        if computer_move == "rock":
           return "Paper covers rock! You win!"
        else:
            return ("Scissors cuts paper! You lose.")
    elif player_move == "scissors":
        if computer_move == "paper":
            return ("Scissors cuts paper! You win!")
        else:
            return ("Rock smashes scissors! You lose.")
