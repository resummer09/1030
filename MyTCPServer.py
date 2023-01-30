# MYTCPServer.py 사용자 정의 모듈

class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('',port)) # 소켓과 주소 결합
        self.sock.listen(1) # 연결 대기 1명
        self.connected = False

    def disconnect(self):
        self.connected = False
        self.c_sock.close()

    def accept(self): # 연결 수락
        self.c_sock, self.c_addr = self.sock.accept()
        self.connected = True
        return self.c_sock, self.c_addr

    def send(self, chat):
        if self.connected:
            self.message = chat
            self.c_sock.send(self.message.encode())
            return True
        else:
            return False

    def receive(self, r_sock=None):
        if not r_sock:
            r_sock = self.c_sock
        try:
            data = r_sock.recv(1024)
            if not data:
                self.disconnect()
                return None
            return data.decode()
        except:
            self.disconnect()
            return None
