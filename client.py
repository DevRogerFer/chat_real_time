import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 55555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()
        self.loaded_window = False
        self.active = True
        self.name = simpledialog.askstring('Nome', 'Digite seu nome:', parent=login)
        self.room = simpledialog.askstring('Sala', 'Digite o nome da sala:', parent=login)
        thread = threading.Thread(target=self.connect)
        thread.start()
        self.window()

    def window(self):
        self.root = Tk()
        self.root.geometry('500x700')  # Janela maior
        self.root.title(f'Chat - {self.name} - {self.room}')
        self.text_box = Text(self.root)
        self.text_box.place(relx=0.05, rely=0.01, width=420, height=570)  # Caixa de texto maior
        self.send_message = Entry(self.root)
        self.send_message.place(relx=0.05, rely=0.85, width=300, height=30)  # Campo de entrada maior
        self.send_button = Button(self.root, text='Enviar', command=self.send_msg)
        self.send_button.place(relx=0.7, rely=0.85, width=80, height=30)
               
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.client.close()
        self.root.destroy()

    def connect(self):
        while True:
            received = self.client.recv(1024)
            if received == b'SALA':
                self.client.send(self.room.encode())
                self.client.send(self.name.encode())
            else:
                try:
                    self.text_box.insert('end', received.decode())
                except:
                    pass

    def send_msg(self):
        message = self.send_message.get()
        self.client.send(message.encode())
        self.send_message.delete(0, 'end') 

chat = Chat()