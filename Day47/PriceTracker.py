import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# allows environment variables from env file
load_dotenv()

# If using static url check website code for changes
static_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0DGHYDZR9/ref=sr_1_1?crid=1F9CE7ZE7XRNW&dib=eyJ2IjoiMSJ9.5Li4-Gl-8nmHyKprPoeN0hrlKyxxRkxteNSXwP56gyq6GFGdGRByZm0QTQvN0taBFRniCbGAhgMLJahuR4kxE7zBDoSGzJwrkML6sBpKwK70575iQA9gF6hIsBbjXfUwRZpTJX1kiz3m0L8k1_AAYSGDcxP6EOQTSMwbA41b2H_-pyHLmXJoshoT0_RcjjP3htqNTnHcaGtXiD5YnJp9uusY26V0Z0f4oLgFRGcKa_8.dsAKT_DiFZVdF-IpkR1piAKwScfRfGRQzBVfGidabh4&dib_tag=se&keywords=iphone+16pro+max&nsdOptOutParam=true&qid=1730818798&sprefix=iphone%2Caps%2C273&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=live_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify()) #For checking code is working

# Getting your product price and removing currency sign
price_current = soup.find(name="span", class_="aok-offscreen").getText().split('₹')[1].split(',')

# This step is for removing commas from price (since it is in INR currency)
price_float = ''
for p in price_current:
    price_float += p

#Set your buying price
buy_price = float(169000)

# Get the product title
product_title = soup.find(id="productTitle").get_text().strip()


# SMTP connection to get email about price drop
if float(price_float) <= buy_price:
    message = f"{product_title} is now at just {price_float}!! Hurry."
    sender = smtplib.SMTP(host="smtp.gmail.com")
    sender.starttls()
    sender.login(user=os.environ["USER_EMAIL"], password=os.environ["USER_PASSWORD"])
    sender.sendmail(from_addr=os.environ["USER_EMAIL"],
                    to_addrs=os.environ["USER_EMAIL"],
                    msg=message)
