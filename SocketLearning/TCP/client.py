import socket
from TCPThread import SendThread, RecvThread

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 本机的ip和端口
    target_ip = '192.168.1.105'
    target_host = socket.gethostname()
    target_port = 9000

    client.connect((target_host, target_port))

    st = SendThread('\nsend: ', client)
    rt = RecvThread('\nrecv: ', client)

    # 启动线程
    st.start()
    rt.setDaemon(True)  # 设置守护线程   后台线程
    rt.start()
