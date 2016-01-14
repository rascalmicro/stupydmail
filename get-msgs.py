import socket

IP = "172.16.10.107"

PORT = 5005

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "received msg: ", data
