from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
list_of_articles = []
article_links = []
for article in articles:
    article_title = article.getText()
    list_of_articles.append(article_title)
    article_link = article.find("a")
    article_link = article_link.get("href")
    article_links.append(article_link)

article_upvotes = [int((score.getText()).split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(list_of_articles)
# print(article_links)
print(article_upvotes)

# highest = article_upvotes.index(max(article_upvotes))
# print(list_of_articles[highest]+" "+article_links[highest]+" "+str(article_upvotes[highest]))
