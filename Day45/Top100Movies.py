from bs4 import BeautifulSoup
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

website_soup = BeautifulSoup(website_html, "html.parser")
movies = website_soup.find_all(name="h3", class_="title")

movies_title = [title.getText() for title in movies]
movies_list = movies_title[::-1]

with open("MoviesList", mode="w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
