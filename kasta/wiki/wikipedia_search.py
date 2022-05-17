import json


class WikiSearch:

    @staticmethod
    def wiki_person(text, key_word):
        person = text.split(key_word, 2)[1].strip()
        print(person)
        return person




