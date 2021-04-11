import socket
from TCPThread import SendThread, RecvThread

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 本机的ip和端口
    ip = '192.168.1.105'
    host = socket.gethostname()
    port = 8081

    s.bind((host, port))
    s.listen(5)  # 等待客户端连接

    while True:
        # con就是客户端链接过来而在服务端为期生成的一个链接实例
        con, addr = s.accept()  # 建立客户端连接

        st = SendThread('\nsend: ', con)
        rt = RecvThread('\nrecv: ', con)

        # 启动线程
        st.start()
        rt.setDaemon(True)  # 设置守护线程   后台线程
        rt.start()
    con.close()  # 关闭连接
