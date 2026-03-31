import socket
import threading

HOST = 'localhost'
PORT = 55555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

rooms = {}

def broadcast(room, message):
    for client in rooms[room]:
        if isinstance(message, str):
            message = message.encode()
        client.send(message)

def send_message(name, room, client_socket):
    while True:
        message = client_socket.recv(1024)
        message = f'{name}: {message.decode()}\n'
        broadcast(room, message)

while True:
    client_socket, addr = server_socket.accept()
    client_socket.send(b'Nome da Sala: ')
    room = client_socket.recv(1024).decode()
    name = client_socket.recv(1024).decode()
    if room not in rooms.keys():
        rooms[room] = []
    rooms[room].append(client_socket)
    print(f'{name} entrou na sala {room}! INFO: {addr}')
    broadcast(room, f'{name} entrou na sala!'.encode())
    thread = threading.Thread(target=send_message, args=(name, room, client_socket))
    thread.start()
