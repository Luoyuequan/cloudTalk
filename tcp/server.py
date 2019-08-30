import socket
import pymysql
from time import localtime
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建首对象

sock.bind(('localhost', 9994))  # 绑定IP、端口号。
sock.listen(5)  # 等待连接队列的最大长度
while True:
    print('等待客户端连接.....\n----------------------------')
    connection, address = sock.accept()  # 客户端请求连接返回新对象、客户端地址
    # print(connection)
    # print(address)
    print('已有客户端连接')
    print('等待对方发送内容!')
    buf = connection.recv(1024)
    print('data', buf, 'type', type(buf), 'length', len(buf))
    buf = buf.decode('utf-8')  # 接受客户端数据
    print('client：', buf.splitlines())
    buf = buf.splitlines()
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "admin_root", "test", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # sql语句
    Sql = "select * from pytest where username='%s'" % (buf[0]);
    print(Sql)
    # 使用 execute()  方法执行 SQL 语句
    cursor.execute(Sql)
    # 使用 fetchone() 方法获取单条数据.
    # 使用 fetchall() 方法获取所有数据.
    datas = cursor.fetchone()
    if datas is None:
        connection.send('此账号不存在!\nfalse'.encode('utf-8'))
    elif datas[2] == buf[1]:
        connection.send('登录成功!\ntrue'.encode('utf-8'))
    elif datas[2] != buf[1]:
        connection.send('密码错误,登录失败!\nfalse'.encode('utf-8'))
    # 提交，不然无法保存新建或者修改的数据
    db.commit()
    # 关闭数据库连接
    db.close()
    # connection.send(content.encode('utf-8'))
    connection.close()
