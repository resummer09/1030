import socket

PORT = 9000
SERVER = '127.0.0.1'
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

print('대 기 중')
while True:
    print("<-", end='')
    data, addr = sock.recvfrom(BUFFSIZE) # 메시지 수신
    print(data.decode()) # 수신 메시지 출력

    resp = input("-> ")
    sock.sendto(resp.encode(), addr) # 메시지 발신