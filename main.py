import os
import requests

NEWS_API = os.getenv("NEWS_API")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-02-04&sortBy=publishedAt&apiKey={NEWS_API}"
request_info = requests.get(url)
content = request_info.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
