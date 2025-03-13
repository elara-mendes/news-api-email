# 📰 news-api-email  

A **Python** script that fetches the latest news from **NewsAPI** and sends them directly to your email via **SMTP**.  

---

## 📌 How the program works  

1. **Fetches news** from an API.  
2. **Automatic translation**: Converts the news description into English.  
3. **Sentiment analysis**: Determines whether the news has a **positive, neutral, or negative** tone.  
4. **Filtering**: Keeps only **positive** news.  
5. **Email delivery**: Sends the best news directly to your inbox.  

---

## ✉️ How to get a Gmail App Password  

Since **Two-Factor Authentication (2FA)** is required for Gmail, you **cannot** use your regular password for SMTP authentication. Instead, you need to generate an **App Password**.  

### 🔧 Steps to enable Two-Factor Authentication and generate an App Password  

1. **Enable Two-Factor Authentication (2FA):**  
   - Go to your [Google Account Security page](https://myaccount.google.com/security).  
   - In the **"How you sign in to Google"** section, select **"2-Step Verification"** and follow the instructions to activate it.  

2. **Generate an App Password:**  
   - Once 2FA is enabled, go back to the **"Security"** section of your account.  
   - Select **"App Passwords"**.  
   - Choose **"Select app"**, then **"Other (Custom name)"**, and enter a name (e.g., `news-bot`).  
   - Click **"Generate"** and save the provided password.  

⚠ **Important:** Store this password securely and **never share it publicly**.  

Copy the generated password and use it in your code.  

In **`send_email.py`**

```python
YOUR_EMAIL = "elaradomingos@gmail.com" # Your email
APP_PASSWORD = os.getenv("GMAIL_PASSWORD") # Your password app
```


---

## ⚙️ Script configuration  

In **`main.py`**, you can customize the **topic**, **language**, and **date** for news retrieval.  

To obtain a **NewsAPI key**, simply create an account here: [NEWS API](https://newsapi.org/). Check the official documentation for further customization based on your needs.  

### 🔧 Example configuration in the code:  

```python
import os

NEWS_API = os.getenv("NEWS_API")  # Your API key
TOPIC = "trans, diversity"  # Search topics
LANGUAGE = "en"  # News language
DATE = "2025-03-06"  # Start date for fetching news (YYYY-MM-DD)
```