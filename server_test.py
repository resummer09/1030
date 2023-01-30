from socket import *

print('--- Socket TCP communication server ---')

Port = 9000 # 서버 포트
encoding = 'utf-8'

# 서버 소켓 생성
Socket = socket(AF_INET, SOCK_STREAM)
# 생성된 소켓과 AF를 [연결] / 빈 문자열이 들어가면 모든 인터페이스와 연결 가능하다는 뜻
Socket.bind(('', Port))
# 클라이언트의 접속을 대기 -- 인자로 최대 동시 접속 가능한 수를 입력
Socket.listen()

print('server is ready')

# 연결 요청을 [수락], 연결된 소켓과 상대방의 주소가 반환됨
connectionSocket, addr = Socket.accept()
print(f'--- connection start with {addr}---')

# 새로운 소켓을 이용해 통신
while True:
    response = connectionSocket.recv(1024)
    print('client <<<', response.decode(encoding))

    chat = input('server >>> ')
    connectionSocket.send(chat.encode(encoding))

connectionSocket.close()