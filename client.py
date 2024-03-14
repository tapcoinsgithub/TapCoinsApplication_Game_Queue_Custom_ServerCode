import asyncio
import websockets
import keyboard

async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        done = False
        while not done:
            if keyboard.is_pressed("space"):
                await websocket.send("buzz")
                message = await websocket.recv()
                print(message)
                done = True
            if keyboard.is_pressed("A"):
                await websocket.send("buzz")
                message = await websocket.recv()
                print(message)
                done = True

asyncio.run(start_client())



# import socket

# HEADER = 64
# PORT = 5050
# SERVER = "10.0.0.194" # socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "!DISCONNECT"

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)