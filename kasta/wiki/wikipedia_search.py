import json


class WikiSearch:

    @staticmethod
    def wiki_person(text):
        if 'wikipedia' in text:
            person = text.split('wikipedia', 2)
            return person[1]
        if 'who is' in text:
            person = text.split('who is', 2)
            return person[1]
        if 'tell me about' in text:
            person = text.split('tell me about', 2)
            return person[1]



