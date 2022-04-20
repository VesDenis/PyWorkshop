import socket

yet_another_socket = socket.socket()
yet_another_socket.connect(('localhost', 1025))
data = b'How deep does the rabbit socket go?'
yet_another_socket.send(data)
buffer_size = 1024
response = yet_another_socket.recv(buffer_size)