import random

response = ['No problem', 'I am here for you', 'You are welcome', 'My pleasure', 'I am Glad to help you', 'Sure',
            'Thak you too']


def thank_you():
    return response[random.randrange(len(response))]
