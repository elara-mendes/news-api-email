import smtplib, ssl
import os

def email_send(message):
    host = "smtp.gmail.com"
    port = 465


    app_password = os.getenv("GMAIL_PASSWORD")

    user_name = "elaradomingos@gmail.com"
    password = app_password
    receiver = "elaradomingos@gmail.com"

    context = ssl.create_default_context()

    message = f"Subject: Today's News\n\n{message}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message.encode("utf-8"))

# if __name__ == "__main__":
#     print(os.getenv("GMAIL_PASSWORD"))

"""
My teacher put the title inside the message, my approach was to use the subject.
Also he's sending all the news in one email, I'm separating each one mail content.
"""