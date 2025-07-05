# MCP Spotify Integration

This repository demonstrates integrating Spotify with a custom MCP server to control playback.

## Features
- Connect to Spotify and control playback
- Search and play tracks programmatically
- Example integration with MCP workflows

## Setup

1. **Clone the repository**
```bash
git clone https://github.com/priyatham1/mcp-spotify.git
cd mcp-spotify
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
Create a `.env` file:
```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

4. **Run the server**
```bash
python3 server.py
```

## Making a request
1. Check the client.py to use it in your custom AI Agent or
2. Add this server to your chat agent


---

🎧 Happy coding!