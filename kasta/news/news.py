import json
import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=eb6b74e2164844e0b23c9669c76999ff')


def tell_news():
    try:
        response = requests.get(url)
    except:
        return "Check your connection"
    news = json.loads(response.text)
    for new in news['articles']:
        return f"{str(new['title'])}\n" + f"{str(new['description'])}"


