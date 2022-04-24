import random

response = [
    'Hello, I am your assistant. I am here to make your life easier. You can command me to perform various tasks.'
    'If you do not know what i can do just say - help me assistant.']

response_robot = [
    'I am not a robot. Robots are telemarketers. They call you to install photovoltaics on the roof of your house',
    'I am not a robot but we live in a simulation and you know it very well or now you started to know it']


class GeneralResponse:

    @staticmethod
    def general_response(text):
        if 'who are you' in text:
            return response[random.randrange(len(response))]
        if 'your name' in text:
            return 'My name is Kasta. How Can i help you'
        if 'who i am' in text:
            return 'You must be a human'
        if 'are you a robot' in text:
            return response_robot[random.randrange(len(response))]
        if 'how are you' in text:
            return 'I am fine, thank you. How are you?'
        if 'i am fine' in text:
            return 'It is good to know that you are fine.'
        if 'i am good' in text:
            return 'It is good to know that you are doing well.'
