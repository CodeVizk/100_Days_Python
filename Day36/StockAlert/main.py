import requests
import datetime as dt
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_key = "4c257e80042a4e11ac45aa4d3f2f40d6"
stock_key = " DINB3K673RXR2GFK"

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
    stock_news_title = news_response.json()["articles"][]
    print(stock_news_title)


stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()


day = dt.datetime.today() - dt.timedelta(1)
yesterday = str(day.date())
day_before = dt.datetime.today() - dt.timedelta(2)
day_before_yesterday = str(day_before.date())

# yesterday_stock = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
# before_yesterday_stock = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
# print(yesterday_stock, before_yesterday_stock)


get_news()

# change_in_stock = abs(yesterday_stock - before_yesterday_stock)
# stock_perc = round((change_in_stock/yesterday_stock) * 100, 2)
# # print(stock_perc)
# if stock_perc >= 5:
#     get_news()

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# 8. - Create a new list of the first 3 article headline and description using list comprehension.
# 9. - Send each article as a separate message via Twilio.


# Optional : Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

