from tmdb import get_popular_movies
from tmdb import get_genres
from tmdb import discover_by_genre
from tmdb import get_imdb_id
from genre_matching import create_genre_dict
from genre_matching import get_genre_id
from dictionaries import create_imdb_id_dict
from dictionaries import create_ratings_dict
from omdb import get_movie_review
import genre_matching

def main(): 
  genres = get_genres()
  genre_dict = create_genre_dict(genres)
  user_genre = input("Enter a movie genre: ")
  genre_id = get_genre_id(user_genre, genre_dict)
  while genre_id is None: 
    user_genre = input("Genre does not exist. Please enter a new genre: ")
    genre_id = get_genre_id(user_genre, genre_dict)
  movies = discover_by_genre(genre_id)
  imdb_id_dict = create_imdb_id_dict(movies)
  print(create_ratings_dict(imdb_id_dict, movies))

if __name__ == "__main__": 
  main()
    
