import socket
from TCPThread import SendThread, RecvThread


class Server():
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def start(self):
        self.server.bind((self.ip, self.port))
        self.server.listen(5)  # 等待客户端连接

        while True:

            # con就是客户端链接过来而在服务端为期生成的一个链接实例
            con, addr = self.server.accept()  # 建立客户端连接
            self.login_check(con)
            st = SendThread('\nsend: ', con)
            rt = RecvThread('\nrecv: ', con)
            # 启动线程
            st.start()
            rt.setDaemon(True)  # 设置守护线程   后台线程
            rt.start()
            print('start server')
        con.close()  # 关闭连接

    def login_check(self, con):
        username = con.recv(2048).decode('utf-8')
        password = con.recv(2048).decode('utf-8')
        admin = ['sun', '123']
        if username not in admin or password not in admin:
            print("Login failed!")
            con.send("Login failed!".encode('utf-8'))
            self.login_check(con)
        else:
            con.send("Login successfully!".encode('utf-8'))


if __name__ == '__main__':
    # 本机的ip和端口
    ip = '192.168.1.105'
    host = socket.gethostname()
    port = 9000
    server = Server(host, port)
    server.start()
