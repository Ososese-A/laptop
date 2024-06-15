import socket

hostname = socket.gethostname()
my_add = socket.gethostbyname(hostname)

print("This is the address", my_add)