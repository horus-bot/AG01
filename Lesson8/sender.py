import socket

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sender.connect(("127.0.0.1", 5000))

print("Connected to receiver!")

message = "pokemon are cool somewhat"

sender.sendall(message.encode())

data = sender.recv(1024)

print("Receiver:", data.decode())

sender.close()


"""address

For example:

('127.0.0.1', 53142)

"""

"""
data = connection.recv(1024)

Now we're actually communicating.

We're saying:

Give me up to 1024 bytes from this TCP connection."""

# import socket

# sender = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sender.connect(("121.00.00.01",5000))
# message="hey"
# sender.sendall(message.encode())

# data = sender.recv(5000)
# print(data.decode())