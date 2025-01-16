
import asyncio
import websockets

async def test_websocket():
    uri = "ws://<service-name>:<port>"  # Replace with your service name and port
    async with websockets.connect(uri) as websocket:
        # Send a test message to the WebSocket server
        await websocket.send("Hello, WebSocket server!")
        
        # Wait for a response from the WebSocket server
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(test_websocket())