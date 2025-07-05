import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8003/mcp")

# Example usage of the MCP client to call the 'play_song' tool
async def main():
    async with client:
        # Get the available tools/operations
        tools = await client.list_tools()
        #print("Available tools:", tools)

        # Call the 'play_song' tool with a song name
        response = await client.call_tool("play_song", {"artist": "Pink Floyd", "song_name": "Wish you were here"})
        print("Response=", response[0].text)



asyncio.run(main())