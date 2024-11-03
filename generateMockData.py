import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Spotify API credentials
CLIENT_ID = '839d0310c3474a8c9d1ca7354f8c5e96'         # Replace with your Spotify Client ID
CLIENT_SECRET = 'b771f53eb6fe4cc288f15d28b44ac762'  # Replace with your Spotify Client Secret

# Setting up Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

CITIES = ['Lancaster', 'Durham', 'Lincoln', 'Luton', 'Glasgow']

# Parameters for song recommendations
GENRES = ['pop', 'rock', 'jazz', 'classical', 'hip-hop', 'country', 'edm', 'blues']
num_tracks = 50
track_ids = []

# Function to get random song recommendations
def get_random_recommendations():
    random_genre = random.choice(GENRES)  # Random genre for variety
    results = sp.recommendations(seed_genres=[random_genre], limit=10)  # Limit each request to 10 songs
    return results['tracks']

# Collecting 100 random song IDs
while len(track_ids) < num_tracks:
    recommendations = get_random_recommendations()
    for track in recommendations:
        track_id = track['id']
        if track_id not in track_ids:  # Avoid duplicates
            track_ids.append(track_id)
        if len(track_ids) >= num_tracks:
            break

# Saving the song IDs to a text file
with open('random_song_ids.txt', 'w') as f:
    for idx, track_id in enumerate(track_ids, start=1):
        f.write(f"{random.choice(CITIES)}, {track_id}\n")