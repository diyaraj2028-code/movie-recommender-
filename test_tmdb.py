import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")

headers = {"Authorization": f"Bearer {api_key}"}

url = f"{api_url}?api_key={api_key}"

response = requests.get(url)

if response.status_code == 200: 
  data = response.json()
  for movie in data.get("results", []): 
    print(movie["title"])
else: 
  print(f"Failed to fetch data. Status code: {response.status_code}")
  print(response.text)