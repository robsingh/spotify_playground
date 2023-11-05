A project to get the list of all of the songs in your Spotify playlists.

Requirements:
 - Python 3
 - Spotipy library

Usage:
1. Install the Spotipy library.
2. Create a Spotify developer account and get a client ID and client secret.
3. Replace the CLIENT_ID and CLIENT_SECRET placeholders in the script with your own credentials.
4. Replace the playlist_uri placeholder with the URI of the playlist that you want to get the tracks for.
5. Run the script. 

How to get the Spotify URI? There are 2 ways. 

Go to the track's page on Spotify.
Right-click on the track and select "Copy link to song".
The link that is copied to your clipboard is the URI of the track.

To get the URI of a Spotify track using the Spotify Web API:

Create a Spotify developer account and get an access token.
Use the following API call to get the URI of the track:
GET https://api.spotify.com/v1/tracks/<TRACK_ID>

Authorization: Bearer <ACCESS_TOKEN>
Replace <TRACK_ID> with the ID of the track that you want to get the URI of.
Replace <ACCESS_TOKEN> with the access token that you got in step 1.

Although I have not implemented the below, but it would be a nice addition to this project, particularly depends on your specific use cases.
1. Use the 'Get a List of Current User's Playlists endpoint'
This returns JSON data with information about all of the playlists of the authenticated users. 

2. Extract the playlist IDs.
From the JSON, you just want to pull out just the playlist ID for each playlist.

3. Use the 'Get a Playlist's items endpoint'
For each playlist ID, make a request to this endpoint, which returns details on all of the tracks in that playlist. 

4. Parse and compile track info
From the track information, extract the details you want like track name, artist name, album, etc and compile them into your master list.

Note to all:
I'd love to hear feedback or suggestions to help me improve this. Feel free to collborate and raise a PR. 
Happy Coding. 








