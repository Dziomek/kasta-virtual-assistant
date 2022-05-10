import json


def load_json(path):
    with open(path) as f:
        data = json.load(f)
    return data


def make_json():
    json_list = [load_json('kasta/date/date_data.json'), load_json('kasta/openApp/openApp_data.json'),
                 load_json('kasta/notification/notification_data.json'), load_json('kasta/wiki/wikipedia_data.json'),
                 load_json('kasta/jokes/jokes_data.json'), load_json('kasta/news/news_data.json'),
                 load_json('kasta/youtube/youtube_data.json'), load_json('kasta/wolfram/wolfram_data.json'),
                 load_json('kasta/greetings/greetings_data.json'),
                 load_json('kasta/general_response/general_response_data.json'),
                 load_json('kasta/acknowledgement/acknowledgement_data.json'),
                 load_json('kasta/weather/weather_data.json'), load_json('kasta/headsortails/headsortails_data.json'),
                 load_json('kasta/spotify/spotify_data.json'),
                 load_json('kasta/rockpaperscisorrs/rockpapersisorrs_data.json'),
                 load_json('kasta/note/note_data.json'), load_json('kasta/read_note/read_note_data.json'),
                 load_json('kasta/send_note_via_email/email_note_data.json'), load_json('kasta/help/help_data.json'),
                 load_json('kasta/googlesearch/googlesearch_data.json'), load_json('kasta/remindMe/reminder_data.json')]

    return json_list
