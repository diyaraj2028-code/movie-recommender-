import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_movie_review(imdb_id): 
  api_key = os.getenv("OMDB_API_KEY")

  api_url = f'http://www.omdbapi.com/?apikey={api_key}&'

  params = {'api_key': api_key, 'i': imdb_id}

  response = requests.get(api_url, params=params)

  if response.status_code == 200: 
    data = response.json()
    return data.get("Ratings") 
  
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)
  return None