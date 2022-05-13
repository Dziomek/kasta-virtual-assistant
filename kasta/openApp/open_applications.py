import webbrowser


class OpenApp:

    @staticmethod
    def open_application(key_word):
        match key_word:
            case "google":
                webbrowser.open_new("https://www.google.com/")
            case "youtube":
                webbrowser.open_new("https://www.youtube.com/")
            case "spotify":
                webbrowser.open_new("https://www.spotify.com/pl/")
            case "wikipedia":
                webbrowser.open_new("https://pl.wikipedia.org/wiki/Wikipedia")
            case "github":
                webbrowser.open_new("https://github.com/")

        '''if "open google" in text:
            webbrowser.open_new("https://www.google.com/")
            return 'i have just opern google chrome'
        if "open chrome" in text:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return 'i have just opern google chrome'
        if "open youtube" in text:
            print('doszlo')
            webbrowser.open("https://youtube.com")
            return 'Opening youtube'
        '''
