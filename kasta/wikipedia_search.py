import wikipedia


class WikiSearch:

    @staticmethod
    def wiki_person(self, text):
        list_wiki = text.split()
        for i in range(0, len(list_wiki)):
            if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == 'who' and list_wiki[i + 1].lower() == 'is':
                return list_wiki[i + 2] + " " + list_wiki[i + 3]
