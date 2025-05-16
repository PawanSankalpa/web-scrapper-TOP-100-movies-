from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_list_web_page = response.text
soup = BeautifulSoup(movie_list_web_page, "html.parser")

all_movies = soup.find_all(name = "h3", class_ = "title")

movie_titles = [movie.getText() for movie in all_movies]

#reversing this list
final_mv_titles_list = movie_titles[::-1]
movies = final_mv_titles_list

with open("movies.txt", mode = "w") as file:
    for  movie in movies:
        file.write(f"{movie}\n")
