import os
import requests
import itertools
from send_email import email_send

NEWS_API = os.getenv("NEWS_API")


url = f"https://newsapi.org/v2/everything?q=trans&language=pt&from=2025-03-03&sortBy=publishedAt&apiKey={NEWS_API}"
request_info = requests.get(url)
content = request_info.json()

message = ""

for article in itertools.islice(content["articles"], 5):
    article_title = article["title"]
    article_description = article["description"]
    article_link = article["url"]
    article_autor = article["author"]
    message += f"Título: {article_title}\nAutor: {article_autor}\n{article_description}\n{article_link}\n\n"
    print(article_title, article_description)


if message is not None:
    email_send(message)