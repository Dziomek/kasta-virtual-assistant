import webbrowser


def search_google(search):
    print(search)
    webbrowser.open_new("https://www.google.com/search?q=" + search)
