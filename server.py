import socket
import threading

HOST = 'localhost'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

rooms = {}

def broadcast(room, message):
    for i in rooms[room]:
        if isinstance(message, str):
            message = message.encode()
        i.send(message)

def send_message(name, room, client):
    while True:
        message = client.recv(1024)
        message = f"{name}: {message.decode()}\n"
        broadcast(room, message)

while True:
    client, addr = server.accept()
    client.send(b'SALA')
    room = client.recv(1024).decode()
    name = client.recv(1024).decode()
    if room not in rooms.keys():
        rooms[room] = []
    rooms[room].append(client)
    print(f'{name} entrou na sala {room}! INFO: {addr}')
    broadcast(room, f'{name} entrou na sala!\n'.encode())
    thread = threading.Thread(target=send_message, args=(name, room, client))
    thread.start()
