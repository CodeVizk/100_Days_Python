# Monaday motivation send a random quote on Monday using smtp and datetime module
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
if now.weekday() == 5:
    print("success")
    with open("quotes.txt") as data:
        quote = data.readlines()

    rand_quote = random.choice(quote)
    print(rand_quote)

    user = "YOUR EMAIL @gmail.com"
    password = "YOUR PASSWORD"

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=user, password=password)
        connect.sendmail(from_addr=user,
                         to_addrs="RECEIVER @gmail.com",
                         msg=f"Subject: Motivational quote for you\n\n{rand_quote}")
