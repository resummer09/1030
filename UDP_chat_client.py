import socket

BUFFSIZE = 1024
PORT = 9000 # 포트 번호

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addr = input('Server IP Address: ') # 같은 컴퓨터에서 실행하면 리턴
if ip_addr == '':
    ip_addr = 'localhost' # 자기 자신 지정
addr = (ip_addr, PORT)

while True:
    msg = input('<- ')
    sock.sendto(msg.encode(), addr) # 메시지 발신
    print('->', end='')
    data, addr = sock.recvfrom(BUFFSIZE) # 메시지 수신
    print(data.decode()) # 수신 메시지 출력
