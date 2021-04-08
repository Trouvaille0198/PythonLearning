import socket  # 导入 socket 模块
import time
from threading import Thread


def send_msg(client):
    # msg = "It's " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    while True:
        msg = input("msg: ")
        client.send(msg.encode('utf-8'))


def recv_msg(client):
    try:
        data = client.recv(1024)  #接收一个信息，并指定接收的大小 为1024字节
        print('recv from server:', data.decode())  #输出我接收的信息
    except:
        pass


client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)  #声明socket类型，同时生成链接对象
host = socket.gethostname()  # 获取本地主机名
port = 6999  # 设置端口号
client.connect((host, port))
while True:
    t1 = Thread(target=send_msg(client), args=(client))
    t2 = Thread(target=recv_msg(client), args=(client))
    t1.start()
    t2.start()
client.close()  #关闭这个链接