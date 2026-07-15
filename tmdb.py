import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_popular_movies(): 
  api_url = 'https://api.themoviedb.org/3/movie/popular'


  api_key = os.getenv("API_KEY")

  params = {'api_key': api_key}

  response = requests.get(api_url, params=params)

  if response.status_code == 200: 
    data = response.json()
    return data 
  
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None

def get_genres(): 
  api_url = 'https://api.themoviedb.org/3/genre/movie/list'

  api_key = os.getenv("API_KEY")
  params = {'api_key': api_key}

  response = requests.get(api_url, params=params)

  if response.status_code == 200: 
    data = response.json()
    return data
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None

def discover_by_genre(genre_id): 
  api_url = 'https://api.themoviedb.org/3/discover/movie'
  api_key = os.getenv("API_KEY")
  params = {'api_key': api_key, 
            'with_genres': genre_id}

  response = requests.get(api_url, params=params)

  if response.status_code == 200: 
    data = response.json()
    return data
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None

def get_imdb_id(movie_id): 
  api_url = f'https://api.themoviedb.org/3/movie/{movie_id}/external_ids'
  api_key = os.getenv("API_KEY")
  params = {'api_key': api_key}

  response = requests.get(api_url, params=params)
  if response.status_code == 200: 
    data = response.json()
    return data.get('imdb_id')
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None

def get_movie_watch_provider(movie_id): 
  api_url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers'
  api_key = os.getenv("API_KEY")
  params = {'api_key': api_key}

  response = requests.get(api_url, params=params)
  if response.status_code == 200: 
    data = response.json()
    print(data)
    return data
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None






