import unittest
import spotipy
from track_list import get_playlist_tracks

class PlaylistTrackTests(unittest.TestCase):
    def test_get_playlist_tracks_with_valid_uri(self):
        playlist_uri = 'URI of the playlist'
        tracks = get_playlist_tracks(playlist_uri)

        self.assertIsInstance(tracks, list)
        self.assertGreater(len(tracks), 0)

    def test_get_playlist_tracks_with_invalid_uri(self):
        playlist_uri = 'playlist_uri'

        with self.assertRaises(spotipy.exceptions.SpotifyException):
            get_playlist_tracks(playlist_uri)
