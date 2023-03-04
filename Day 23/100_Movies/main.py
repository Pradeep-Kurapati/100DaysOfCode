import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.timeout.com/film/best-movies-of-all-time")
data = response.content

soup = BeautifulSoup(data, "html.parser", from_encoding='utf-8')

movies = soup.find_all(name="h3", class_="_h3_cuogz_1")
movie_list = []
for x in movies:
    name = x.text
    name = name.replace(u'\xa0', u' ')
    movie_list.append(name)

print(movie_list)

with open('100_movies.txt', mode="w") as file:
    for x in movie_list:
        file.write(x)
        file.write('\n')


# movies = soup.find_all(name="h3", class_="jsx-4245974604")
# print(movies)

# movie_list = []
# for movie in movies:
#     movie_list.append(movie.getText())
#
# print(movie_list)
