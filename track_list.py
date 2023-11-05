import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_uri):
    """
    Get the list of all the tracks in the Spotify playlist.

    Args:
        playlist_uri : URI of the specified playlist.

    Returns:
        A list of all the tracks in the Spotify playlist.
    """
    offset = 0
    tracks = []
    
    while True:
        response = sp.playlist_tracks(playlist_uri, offset=offset)
        if len(response['items']) == 0:
            break
        tracks += response['items']
        offset += 100

    return tracks


playlist_uri = 'playlist URI'
tracks = get_playlist_tracks(playlist_uri)

for track in tracks:
    print(track['track']['name'])
