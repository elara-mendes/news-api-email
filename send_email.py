import smtplib, ssl
import os

YOUR_EMAIL = "elaradomingos@gmail.com"
APP_PASSWORD = os.getenv("GMAIL_PASSWORD")


def email_send(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = YOUR_EMAIL
    password = APP_PASSWORD
    receiver = YOUR_EMAIL

    context = ssl.create_default_context()

    message = f"Subject: Today's News\n\n{message}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message.encode("utf-8"))