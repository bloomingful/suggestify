import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()

# Credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
user_id = "12146041535"
playlist_id = "7J0kact8iZpiW1Wkeksqbq"

# Set up Spotipy with user authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-read-private"))

# Fetch the playlist tracks
results = sp.playlist_tracks(playlist_id)

# Extract and print the song titles and IDs
# for idx, item in enumerate(results["items"]):
#     track = item["track"]
#     print(f"{idx + 1}. {track['name']} (ID: {track['id']})")

# Create a dictionary of song titles and IDs
tracks_dict = {}
for item in results['items']:
    track = item['track']
    title = track['name']
    track_id = track['id']
    tracks_dict[title] = track_id

# Set up client credentials
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)

# Set up Spotipy with client credentials
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Fetch the audio features
for track_title, track_id in tracks_dict.items():
    audio_features = sp.audio_features(track_id)
    tracks_dict[track_title] = audio_features[0]

print(list(tracks_dict["Naked Heart"].keys()))

# Remove unnecessary fields
for track in tracks_dict:
    del tracks_dict[track]['id']
    del tracks_dict[track]['type']
    del tracks_dict[track]['uri']
    del tracks_dict[track]['track_href']
    del tracks_dict[track]['analysis_url']
    del tracks_dict[track]['duration_ms']
    del tracks_dict[track]['time_signature']