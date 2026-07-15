from tmdb import get_imdb_id
from omdb import get_movie_review

def create_imdb_id_dict(genre_movie_dict):
  imdb_id_dict = {}
  for movie in genre_movie_dict.get('results', []): 
    imdb_id = get_imdb_id(movie['id'])
    if imdb_id == None: 
      continue 
    imdb_id_dict[movie['id']] = imdb_id
  return imdb_id_dict

def create_ratings_dict(imdb_dict, genre_movie_data): 
  ratings_dict = {}
  for id in imdb_dict: 
    ratings = get_movie_review(imdb_dict[id])
    if ratings == [] or ratings == None: 
      continue 
    for movie in genre_movie_data.get('results', []): 
      if movie['id'] != id: 
        continue 
      title = movie['title']
      ratings_dict[title] = 'Rating not found'
      for rating in ratings: 
        if rating['Source'] == 'Metacritic': 
          ratings_dict[title] = rating['Value']
  return ratings_dict