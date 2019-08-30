import socket
import demjson


#################################################
# 说明：构造TCPclient调用类
# 功能；TCPclient实例化，发送数据，接收数据
# TCPclient类实例化_参数：TCPserver address，port
# 发送数据_参数：需发送数据
#################################################
class clientTcp:
    def __init__(self, host='127.0.0.1', port=11111):
        self.sock = None  # 存储实例化客户端对象
        self.host = host  # 服务端地址
        self.port = port  # 端口号
        # self.receiveData=''                   #接收的数据
        self.connect()


    # 开始连接
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        # self.sock.setblocking(0)
        # return self.sock

    # 断开连接
    def close(self):
        self.sock.close()

    # 发送数据
    def sendData(self, data):
        # 数据进行编码 a bytes-like object
        # 将 Python 对象编码成 JSON 字符串
        data = demjson.encode(data)
        # 返回值为数据长度
        resulte = self.sock.send(data.encode())
        if len(data) == resulte:
            return True
        else:
            return False

    # 接收数据
    def receiveData(self, bufsize=1024):
        data = self.sock.recv(bufsize)
        # 将已编码的 JSON 字符串解码为 Python 对象
        data = data.decode()
        # print(data,type(data),len(data))
        data = demjson.decode(data)
        # print(data,type(data),len(data))
        return data
        # except Exception as jsonError:
        #     print("jsonError:")



    # 进行堵塞式接收数据
    def returnSock(self):
        return self.sock

# def main():
#     client = clientTcp()
#     # while True:
#     # data = client.receiveData()
#     # print(data)
#     data = {'username': '123456', 'password': '123456', 'action': 'Login'}
#     print(data,type(data))
#     resulte = client.sendData(data)
#     print(resulte)
#     data = client.receiveData()
#     print("data:{0},type:{1},len:{2}".format(data, str(type(data)), len(data)))
#     # time.sleep(2)
#     client.close()
#
#
# main()
