import pywhatkit
from PySide2.QtCore import QThread


def play_on_yt(text, key_word):
    movie = text.split(key_word, 2)
    pywhatkit.playonyt(movie[1])




