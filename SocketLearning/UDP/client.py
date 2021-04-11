import socket
from UDPThread import SendThread, RecvThread


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 本机的ip和端口
    ip = '192.168.1.105'
    host = socket.gethostname()
    port = 9000
    # 目标主机的ip和端口
    target_host = socket.gethostname()
    target_ip = '192.168.1.101'
    target_port = 9000
    # 绑定
    client.bind((host, port))
    st = SendThread('\nsend: ', client, target_ip, target_port)
    rt = RecvThread('\nrecv: ', client)

    # 启动线程
    st.start()
    rt.setDaemon(True)  # 设置守护线程   后台线程
    rt.start()
