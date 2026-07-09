from  tmdb import get_genres

def create_genre_dict(data): 
  name_to_ids = {}
  for genre in data.get('genres', []):
    name_to_ids[genre['name'].lower()] = genre['id']
  return name_to_ids

def get_genre_id(user_input, genre_dict): 
  new_input = user_input.lower()
  if new_input not in genre_dict: 
    return None 
  return genre_dict[new_input]
