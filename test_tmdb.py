import requests
import os
from dotenv import load_dotenv

API_URL='https://api.themoviedb.org/3/movie/popular'

load_dotenv()

api_key = os.getenv("API_KEY")

params = {'api_key': api_key}

response = requests.get(API_URL, params=params)

if response.status_code == 200: 
  data = response.json()
  for movie in data.get("results", []): 
    print(movie["title"])
else: 
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)