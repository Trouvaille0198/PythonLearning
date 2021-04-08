import socket
from threading import Thread


def send_msg(con):
    while True:
        msg = input('msg: ')
        con.send(msg.encode('utf-8'))


def recv_msg(con):
    try:
        data = con.recv(1024)  #接收数据
        print('recive from client:', data.decode())  #打印接收到的数据
    except:
        pass


# type(套接字类型) SOCK_STREAM(TCP协议) SOCK_DGRAM(UDP协议)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 6999  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    # con就是客户端链接过来而在服务端为期生成的一个链接实例
    con, addr = s.accept()  # 建立客户端连接
    while True:
        try:
            data = con.recv(1024)  #接收数据
            print('recive from client:', data.decode())  #打印接收到的数据
            msg = input('msg: ')
            con.send(msg.encode('utf-8'))  #然后再发送数据
        except:
            print('connection failed!')
            break

# while True:
#     con, addr = s.accept()
#     t1 = Thread(target=send_msg(con), args=(con))
#     t2 = Thread(target=recv_msg(con), args=(con))
#     while True:
#         try:
#             t2.start()
#             t1.start()

#         except:
#             print('connection failed!')
#             break

con.close()  # 关闭连接
