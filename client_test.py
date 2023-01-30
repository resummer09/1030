from socket import *

print('--- Socket TCP communication client ---')

Name = '127.0.0.1' # 서버이름(로컬)
Port = 9000       # 포트번호
encoding = 'utf-8'

# 클라이언트 소켓 [생성] -- IPv4와의 TCP 통신을 위한 스트림 소켓
clientSocket = socket(AF_INET, SOCK_STREAM)
# 서버에게 소켓 [연결] 요청
clientSocket.connect((Name, Port))

print(f'--- connected with server {Name}:{Port} ---')
while True:
    chat = input('client >>>')
    clientSocket.send(chat.encode(encoding))
    response = clientSocket.recv(1024)
    print(f'server <<< {response.decode(encoding)}')

# clientSocket.close()