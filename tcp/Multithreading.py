# # Multithreading concurrent processing
# # 多线程并发处理
#
# import socketserver
# import subprocess
#
#
# class MyServer(socketserver.BaseRequestHandler):  # 继承
#     def handle(self):  # handle方法。注意此时send和recv时调用的self.request方法
#         self.request.sendall(bytes('Welcome', encoding='utf-8'))
#         while True:
#             try:
#                 recv_data = self.request.recv(1024)
#                 print(recv_data)
#                 if not recv_data: break
#                 p = subprocess.Popen(str(recv_data, encoding='utf-8'), shell=True, stdout=subprocess.PIPE,
#                                      stderr=subprocess.PIPE)
#                 print(p)
#                 res = p.stdout.read()
#                 print(type(res), len(res), res)
#                 if not res:
#                     send_data = p.stderr.read()
#                     print(send_data)
#                 else:
#                     send_data = res
#                 if not send_data:
#                     send_data = 'no output'.encode()
#
#                 print(type(send_data), len(send_data), send_data)
#                 data_size = len(send_data)
#                 print(data_size)
#                 print(bytes(str(data_size), encoding='utf-8'))
#                 print(1, type(self.request.send(bytes(str(data_size), encoding='utf-8'))), self.request.send(bytes(str(data_size), encoding='utf-8')))
#                 print(2,self.request.recv(1024))
#                 print(3,self.request.send(send_data))
#             except Exception:
#                 break
#
#
# # if __name__ == '__main__':
# server = socketserver.ThreadingTCPServer(('127.0.0.1', 9998), MyServer)  # 启动server
# server.serve_forever()
#
# # 实现socketserver运行的代码
# server端
# 导入该模块
import socketserver


# 定义一个类，继承socketserver.BaseRequestHandler
class Server(socketserver.BaseRequestHandler):
    def handle(self):
        # 打印客户端地址和端口
        print('New connection:', self.client_address)
        # 循环
        while True:
            # 接收客户发送的数据
            data = self.request.recv(1024)
            if not data: break  # 如果接收数据为空就跳出，否则打印
            print('Client data:', data.decode())
            self.request.send(data)  # 将收到的信息再发送给客户端


if __name__ == '__main__':
    host, port = '127.0.0.1', 9998  # 定义服务器地址和端口
    server = socketserver.ThreadingTCPServer((host, port), Server)  # 实现了多线程的socket通话
    server.serve_forever()  # 不会出现在一个客户端结束后，当前服务器端就会关闭或者报错，而是继续运行，与其他的客户端继续进行通话。

# # client端
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# sk = socket.socket()
# sk.connect(ip_port)
#
# while True:
#     raw = input('>> ').strip()
#     sk.send(bytes(raw, 'utf8'))
#     msg = sk.recv(1024)
#     print(str(msg, 'utf8'))
# sk.close()
