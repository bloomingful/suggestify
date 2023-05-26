import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your own credentials and playlist ID
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "your_redirect_uri"
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
for idx, item in enumerate(results["items"]):
    track = item["track"]
    print(f"{idx + 1}. {track['name']} (ID: {track['id']})")