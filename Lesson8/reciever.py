import socket

receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

receiver.bind(("127.0.0.1", 5000))
receiver.listen()

print("Waiting for sender...")

connection, address = receiver.accept()

print("Sender connected:", address)

data = connection.recv(1024)

print("Sender:", data.decode())

reply = "Hello sender! Message received."

connection.sendall(reply.encode())

connection.close()
receiver.close()