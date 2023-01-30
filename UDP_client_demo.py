import socket

PORT = 9000
BUFFSIZE = 1024
SERVER = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello UDP server WORLD :) "
sock.sendto(msg.encode(), (SERVER, PORT)) # 서버에 메시지 전송

data, addr = sock.recvfrom(BUFFSIZE)
print('Server says: ', data.decode()) # 서버의 응답

