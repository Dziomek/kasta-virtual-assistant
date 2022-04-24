class WikiSearch:

    @staticmethod
    def wiki_person(text):
        if 'wikipedia' in text:
            person = text.split('wikipedia', 2)
            return person[1]




