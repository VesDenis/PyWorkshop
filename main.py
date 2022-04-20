import socket

your_sock = socket.socket()
your_sock.connect(('deepthought.com', 4242))
question = b'The answer to the meaning of life'
your_sock.send(question)