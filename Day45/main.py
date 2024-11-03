from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# To get every item of same tags use find_all(name="XYZ")
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    pass

# to get the first item that matches our query use find(name="")

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

name = soup.find_all("h3", class_="heading")
# print(name)

selector = soup.select_one(selector="p a")
# print(selector)


headings = soup.select(selector=".heading")
# print(headings)