import os
import requests
import itertools
from send_email import email_send

NEWS_API = os.getenv("NEWS_API")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-02-04&sortBy=publishedAt&apiKey={NEWS_API}"
request_info = requests.get(url)
content = request_info.json()

for article in itertools.islice(content["articles"], 1):
    article_title = article["title"]
    article_description = article["description"]
    email_send(article_title, article_description)
    print(article_title, article_description)