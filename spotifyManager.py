import spotipy
import dataman
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

REDIRECT_URI = "http://localhost:5000/index"
SCOPE = "user-top-read user-library-read user-read-email user-read-private"

SPOTIPY_CLIENT_ID='839d0310c3474a8c9d1ca7354f8c5e96'
SPOTIPY_CLIENT_SECRET='b771f53eb6fe4cc288f15d28b44ac762'

sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
)

def get_artist_image(track_id):
    sp = spotipy.Spotify(auth_manager = sp_oauth)
    track = sp.track(track_id)
    artist_id = track['artists'][0]['id']
    artist = sp.artist(artist_id)
    if not(artist['images']):
        return "---"
    return artist['images'][0]['url']

def get_top_songs(myAuth):
    token = sp_oauth.get_access_token(myAuth)
    sp = spotipy.Spotify(auth=token['access_token'])
    user = sp.current_user()
    topTracks = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')
    tracks = []
    for item in topTracks['items']:
        tracks.append(item['id']+"@"+get_artist_image(item['id']))
    return ":::".join(tracks)

def add_top_songs(myAuth, lat, long):
    token = sp_oauth.get_access_token(myAuth)
    sp = spotipy.Spotify(auth=token['access_token'])
    user = sp.current_user()
    topTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
    tracks = []
    for item in topTracks['items']:
        dataman.add_entry(lat, long, item['id'])