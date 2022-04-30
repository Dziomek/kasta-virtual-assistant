import random


def helpMe():
    response = ["You can ask me many things! "
                "for example, who is Robert Lewandowski, "
                "what time is it, "
                "make a note, "
                "tell a joke, "
                "play rock paper scissors, "
                "and much much more "]
    return response[random.randrange(len(response))]
