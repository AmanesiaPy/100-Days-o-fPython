from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="a", class_="storylink")
article_text = []
article_link = []
for tags in article_tag:
    text = tags.getText()
    article_text.append(text)
    link = tags.get("href")
    article_link.append(link)
article_upvote = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]
print(article_text)
print(article_link)
print(article_upvote)
max_upvote = article_upvote.index(max(article_upvote))
print(article_text[max_upvote])
print(article_link[max_upvote])
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
