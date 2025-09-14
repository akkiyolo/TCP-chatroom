import socket
import threading

host='127.0.0.1' # localhost
port = 55555

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[] # clients that would be connecting to the server
nicknames=[] # nicknames of clients that clients can choose

## sends a message to all the clients that are connected to the server
def broadcast(message): 
  for client in clients:
    client.send(message)

## handle the client connection if client is sending any messages 
def handle(client):
  while True:
    try: ## try to receive a message from the client and if that succeed broadcast it to all other clients
      message = client.recv(1024) 
      broadcast(message)
    except: 
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname=nicknames[index]
      broadcast(f"{nickname} left the chat!".encode('ascii'))
      nicknames.remove(nickname)
      break

def receive(): ## receiving client connections
  while True:
    client, address = server.accept()
    print(f"Connected with {str(address)}")

    client.send('NICK'.encode('ascii'))
    nickname= client.recv(1024).decode('ascii')
    nicknames.append(nickname)  # Fixed: append nickname to nicknames list
    clients.append(client)

    print(f'Nickname of the client: {nickname}!')
    broadcast(f'{nickname} joined the chat!'.encode('ascii'))
    client.send('connected to the server'.encode('ascii'))

    thread = threading.Thread(target=handle,args=(client,))
    thread.start()

print("server is listening...")
receive()