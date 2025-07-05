import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fastmcp import FastMCP
import os
from dotenv import load_dotenv


# Spotify configuration

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:8888/callback")
SCOPE = "user-read-playback-state user-modify-playback-state"

mcp = FastMCP(name="Spotify Music MCP Server")

@mcp.tool
def play_song(song_name: str, artist: str) -> str:
    """
    Play a specific song on Spotify (needs a Premium account).

    Args:
        song_name (str): The name of the song.
        artist (str): The artist name.

    Returns:
        str: Status message indicating success or failure.
    """

    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

    # Build search query
    query = f"track:{song_name}"
    if artist:
        query += f" artist:{artist}"

    # Search for track
    results = sp.search(q=query, type="track", limit=1)
    tracks = results.get("tracks", {}).get("items", [])

    if not tracks:
        return f" Track '{song_name}' by '{artist}' not found."

    track_uri = tracks[0]["uri"]
    found_name = tracks[0]["name"]
    found_artist = tracks[0]["artists"][0]["name"]

    # Get active devices
    devices = sp.devices()
    device_list = devices.get("devices", [])
    if not device_list:
        return "No active Spotify devices found. Please open Spotify app first on your macbook."

    # Use first active device
    device_id = device_list[0]["id"]

    # Start playback
    sp.start_playback(device_id=device_id, uris=[track_uri])
    return f" Playing '{found_name}' by {found_artist} on {device_list[0]['name']}."


if __name__ == "__main__":
    # Start the server
    # You can access the server at http://localhost:8003
    mcp.run(
        transport="http",
        port=8003,
        )
    print("Spotify Music MCP Server has started. Access it at http://localhost:8003/mcp") 