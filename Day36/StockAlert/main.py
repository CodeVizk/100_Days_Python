import requests
import datetime as dt
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_key = "YOUR KEY"
stock_key = "YOUR KEY"

# Use https://www.alphavantage.co/documentation/#daily
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_key
}


news_params = {
    "apikey": news_key,
    "q": COMPANY_NAME,
    "language": "en"

}


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    stock_news = news_response.json()["articles"]
    stock_article = stock_news[:3]

    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in stock_article]

    user = "YOUR EMAIL"
    password = "YOUR PASSWORD"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=user, password=password)
    connection.sendmail(from_addr=user,
                        to_addrs="RECEIVER",
                        msg=f"Subject:Stock Update\n\nTSLA:{up_down}{stock_perc}\n{formatted_article}"
                        )


get_news()
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()


day = dt.datetime.today() - dt.timedelta(1)
yesterday = str(day.date())
day_before = dt.datetime.today() - dt.timedelta(2)
day_before_yesterday = str(day_before.date())

yesterday_stock = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_stock = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
print(yesterday_stock, before_yesterday_stock)

change_in_stock = yesterday_stock - before_yesterday_stock
stock_perc = round((change_in_stock/yesterday_stock) * 100)

up_down = None
if change_in_stock > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


if abs(stock_perc) >= 5:
    get_news()
