# 요청 처리 서버 프로그램

import socket
#숫자에 대한 영어 사전
table = {'1':'one', '2':'two', '3':'three', '4': 'four',
         '5':'five', '6':'six','7':'seven', '8':'eight',
         '9':'nine', '10':'ten'}

s = socket.socket() #AF_INET, SOCK_STREAM
address = ('', 9000)

s.bind(address) # 주소에 바인딩
s.listen(1) # 동시접속 1명
print('대기중')

c_socket, c_addr = s.accept() # 연결된 소켓, 주소를 accept로 받아옴
print('connecting :', c_addr)
while True:
    data = c_socket.recv(1024).decode() # 요청 수신
    try:
        resp = table[data] # 데이터를 key로 사용하여 value를 가져온다
    except:
        c_socket.send('Try again'.encode()) # 오류가 있을 때
    else:
        c_socket.send(resp.encode()) # 변환 값을 전송