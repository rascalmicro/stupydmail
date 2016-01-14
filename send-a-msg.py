import socket

IP ="172.16.10.107"
PORT = 5005

MESSAGE = "Whatever"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (IP, PORT))

