from bs4 import BeautifulSoup
import requests

response = requests.get('https://empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

all_movies = soup.find_all(name='h2')
movie_titles = [movie.getText() for movie in all_movies]
remove_unnecessary_title = movie_titles[1::]
final_movie_list = remove_unnecessary_title[::-1]


with open('movie_list.txt', 'w') as file:
    file.write('\n'.join(final_movie_list))

