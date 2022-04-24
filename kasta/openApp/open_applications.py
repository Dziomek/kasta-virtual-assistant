import os
import webbrowser

class OpenApp:

    @staticmethod
    def OpenAplication(text):
        if "open google chrome" in text:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return 'i have just opern google chrome'
        if "open chrome" in text:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return 'i have just opern google chrome'
        if "open youtube" in text:
            print('doszlo')
            webbrowser.open("https://youtube.com")
            return 'Opening youtube'
