from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
# print(soup.title.string)

all_a_tags = soup.find_all(name="a")

# for tag in all_a_tags:
    # print(tag)


heading = soup.find(name="h1", id="name")
# print(heading)

body = soup.find(name="h3", class_="heading")
# print(body.get_text())

c_url = soup.select_one(selector="p a")
# print(c_url)

c_name = soup.select_one(selector="#name")
# print(c_name)

class_heading = soup.select(".heading")
print(class_heading)
