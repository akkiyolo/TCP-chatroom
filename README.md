# TCP-chatroom

 <img src ="Screenshot 2025-09-14 151327.png"/>

## 🔧 How It Works
The application follows a simple client-server model:

** server.py: The central hub. It listens for incoming connections, accepts new clients, and manages the list of connected users. When the server receives a message from any client, it uses a broadcast function to relay that message to every other connected client. Each client connection is handled in a separate thread to manage them concurrently.

** client.py: The user-facing application. When launched, it prompts the user for a nickname and connects to the server. It uses two threads: one for listening for incoming messages from the server and printing them to the console, and another for capturing user input and sending it to the server.
