import socket

PORT = 9000
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP소켓
sock.bind(('', PORT))
print('수신 대기')

while True:
    data, addr = sock.recvfrom(BUFFER) # 데이터와 상대방 종단점 주소 수신
    print("받은 메시지: ", data.decode())
    print("주소: ", addr)
    sock.sendto(data, addr) # 상대 주소로 수신 메시지를 재전송