import random

response = [
    'Hello, I am your assistant. I am here to make your life easier. You can command me to perform various tasks. '
    'If you do not know what i can do just say - help me assistant.']

response_robot = [
    'I am not a robot. Robots are telemarketers. They call you to install photovoltaics on the roof of your house',
    'I am not a robot but we live in a simulation and you know it very well or now you started to know it']


class GeneralResponse:

    @staticmethod
    def general_response(key_word):
        if 'who are you' in key_word:
            return response[random.randrange(len(response))]
        elif 'your name' in key_word:
            return 'My name is Kasta. How Can i help you'
        elif 'who i am' in key_word:
            return 'You must be a human'
        elif 'are you a robot' in key_word:
            return response_robot[random.randrange(len(response))]
        elif 'how are you' in key_word:
            return 'I am fine, thank you. How are you?'
        elif 'i am fine' in key_word:
            return 'It is good to know that you are fine.'
        elif 'i am good' in key_word:
            return 'It is good to know that you are doing well.'
        elif "i'm good" in key_word:
            return 'It is good to know that you are doing well.'
        elif "i'm fine" in key_word:
            return 'It is good to know that you are fine.'
