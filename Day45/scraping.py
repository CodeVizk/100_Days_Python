# Since we are scraping from a live website the code might not work everytime

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []

for tag in articles:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)


article_upvotes = [int(votes.getText().split()[0]) for votes in soup.find_all(name="span", class_="score")]

# print(article_links)
# print(article_texts)
# print(article_upvotes)

largest_vote = max(article_upvotes)
largest_index = article_upvotes.index(largest_vote)
mvpost = article_texts[largest_index]
mvlink = article_links.index[largest_index]

print(mvpost, mvlink)
