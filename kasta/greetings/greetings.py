import random

def sayHello():
    response = ["It's pleasent to have you on board. How can I help you?", "Hi, I am ready for your commands", "Hello, i hope you are doing well", "You are gorgeous. How can i help you?","It is beautiful day to ask me something"]
    return response[random.randrange(len(response))]
