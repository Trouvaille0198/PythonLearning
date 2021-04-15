import socket
from TCPThread import SendThread, RecvThread


class Client():
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def connect(self):
        self.client.connect((self.ip, self.port))

    def start(self):
        st = SendThread('\nsend: ', self.client)
        rt = RecvThread('\nrecv: ', self.client)
        # 启动线程
        st.start()
        rt.setDaemon(True)  # 设置守护线程/后台线程
        rt.start()

    def login(self):
        username = input("Please input your username: ")
        password = input("please input your password: ")
        self.client.send(username.encode('utf-8'))
        self.client.send(password.encode('utf-8'))
        res = self.client.recv(2048).decode('utf-8')
        print(res)
        if res == 'Login successfully!':
            pass
        else:
            self.login()


if __name__ == '__main__':
    # 本机的ip和端口
    target_ip = '192.168.1.105'
    target_host = socket.gethostname()
    target_port = 9000

    client = Client(target_host, target_port)
    client.connect()
    client.login()
    client.start()
