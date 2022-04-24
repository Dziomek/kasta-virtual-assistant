import pandas as pd
from speech_recognition import Microphone, Recognizer, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

from kasta.spotify.pepper import get_track_uri, get_album_uri, play_album, InvalidSearchError, play_track, play_artist, \
    get_artist_uri


client_id = 'a695640508154c118d601cd3221fe70c'
client_secret = 'c836c79df2e04d54aada1caf368e6dcc'
device_name = 'DESKTOP-T35AE2C'
redirect_uri = 'https://example.com/callback/'
username = '11133499002'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

class PlaySpotify():
    def __init__(self):
        # Connecting to the Spotify account
        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            username=username)
        self.spotify = sp.Spotify(auth_manager=auth_manager)

        # Selecting device to play from
        devices = self.spotify.devices()
        self.deviceID = None
        for d in devices['devices']:
            d['name'] = d['name'].replace('’', '\'')
            if d['name'] == device_name:
                self.deviceID = d['id']
                break

    @staticmethod
    def spotify(text,self):
        if 'play' in text:
            words = text.split()
            print(words)
            name = ' '.join(words[1:0])
            print(name)
            try:
                if words[0] == 'album':
                    uri = get_album_uri(spotify=self.spotify, name=self.name)
                    play_album(spotify=self.spotify, device_id=self.deviceID, uri=uri)
                elif words[0] == 'artist':
                    uri = get_artist_uri(spotify=self.spotify, name=name)
                    play_artist(spotify=self.spotify, device_id=self.deviceID, uri=uri)
                elif words[0] == 'play':
                    uri = get_track_uri(spotify=self.spotify, name=name)
                    play_track(spotify=self.spotify, device_id=self.deviceID, uri=uri)
                else:
                    print('Specify either "album", "artist" or "play". Try Again')
            except InvalidSearchError:
                print('InvalidSearchError. Try Again')


cos = PlaySpotify
cos.spotify('play mata',)





