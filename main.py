import requests
import itertools
from deep_translator import GoogleTranslator
from send_email import email_send
from textblob import TextBlob
import os

NEWS_API = os.getenv("NEWS_API") # Your API key
TOPIC = "trans, diversity"
LANGUAGE = "en"
DATE = "2025-03-06"  # YYYY-MM-DD / From date till today

url = f"https://newsapi.org/v2/everything?q={TOPIC}&language={LANGUAGE}&from={DATE}&sortBy=publishedAt&apiKey={NEWS_API}"
request_info = requests.get(url)
content = request_info.json()


def translation_content(text):
    if LANGUAGE.lower() == "pt":
        translated = GoogleTranslator(source="pt", target='en').translate(text)
    else:
        translated = GoogleTranslator(source=LANGUAGE, target='en').translate(text)
    return translated


def text_sentiment():
    sentiments = []
    for article in itertools.islice(content["articles"], 10):
        article_title = article["title"]
        article_description = article["description"]
        article_link = article["url"]
        if article_title is not None:
            translated_text = translation_content(article_description)
            content_text = TextBlob(translated_text)
            content_polarity = content_text.polarity
            if content_polarity > 0:
                sentiments.append({
                    "title": article_title,
                    "description": article_description,
                    "link": article_link
                })
    return sentiments


positive_news = text_sentiment()

message = ""
for articles in positive_news:
    message += f"""
    Título: {articles["title"]}\n
    {articles["description"]}\n
    {articles["link"]}\n
"""

print(message)  # Preview

if message is not None:
    email_send(message)
