import socket
from SocketLearning.UDP.UDPThread import SendThread, RecvThread


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = '127.0.0.1'
    port = 9000
    client.bind((ip, port))
    st = SendThread('send: ', client, '127.0.0.1', 8700)
    rt = ReceiverThread('recv: ', client)

    # 启动线程
    st.start()
    rt.setDaemon(True)  # 设置守护线程   后台线程
    rt.start()
