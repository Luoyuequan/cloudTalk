import socket
import select
import pymysql
import time

sk = socket.socket()
ip_port = ("localhost", 9999)
sk.bind(ip_port)
sk.listen(5)

inputs = [sk, ]  # 定义监听的对象列表。默认只监听服务端socket对象
outputs = []  # 定义消息输出列表
message = {}  # 定义一个字典，用于记录客户端对象和收到的消息  key为客户端对象，value为消息 实时消息
oldMessage = {}  # 记录从客户端收到的消息，key为时间y-m-d h，value为消息，历史消息
while True:  # 循环检测对象
    # 监听sk(服务端)对象,如果sk发生变化,表示有新连接来了,此时rlist的值为sk
    rlist, wlist, e = select.select(inputs, outputs, [], 1)
    # print("inputs:", len(inputs), "rlist:", len(rlist), "outputs:", len(outputs), "wlist:", len(wlist))
    #  打印inputs 便于查看效果 print(inputs, rlist, outputs, wlist) 读数据
    for i in rlist:  # 循环变化的列表，然后对每个对象进行操作
        if i == sk:  # 如果是服务端socket对象发生变化，表示新连接建立了
            conn, ip = sk.accept()  # 建立连接
            inputs.append(conn)  # 将新建立的连接加入监听的列表中
            message[conn] = []  # 创建关于新连接的key
            # 判断记录历史客户端消息字典中key是否已存在
            # if conn.getpeername()[0] in oldMessage.keys():
            #     pass
            # else:
            #     oldMessage[conn.getpeername()[0]] = []  # 创建记录历史客户端消息的key
            # print(conn)
            # try:
            #     print(conn.getsockname(), conn.getpeername()[0])
            # except Exception as connError:
            #     print('connError:', connError)
            # print(ip)
        else:  # 否则是客户端给服务端发消息了。所以需要收消息
            try:
                recv_data = i.recv(1024).decode('utf-8')  # 接受数据
                # currentTime = time.strftime("%Y-%m-%d %H", time.localtime())
                # print(currentTime)
                # recv_data=recv_data+'\n'+currentTime
                # print(recv_data)
                if not recv_data:  # 判断数据是否为空
                    # print('没有数据')
                    # time.sleep(5)
                    # inputs.remove(i)  # 将发消息的对象从监听对象列表中移除
                    # pass
                    raise Exception("disconnect")  # 为空的话，主动抛出异常
                else:
                    outputs.append(i)  # 将发消息的对象存入outputs
                    message[i].append(recv_data)  # 将发消息的对象和消息存入message
                    # print(message, type(message))
            except Exception as RecvError:
                # print('RecvError:', RecvError)
                inputs.remove(i)  # 捕捉到异常，客户端断开连接，则在监控列表中删除此对象
                del message[i]  # 在消息字典中删除此对象key/value
                # print(inputs, rlist, outputs, wlist)
    # 发数据
    for i in wlist:  # 循环wlist列表。如果wlist列表中有值的话，说明收到客户端消息
        try:
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "admin_root", "test", charset="utf8")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 取出该客户端对象发的消息，并在列表中删除
            msg = message[i].pop()
            # 账号与密码和请求操作进行分割，组成列表
            msg = msg.splitlines()
            # 请求操作为登录
            if msg[2] == 'Login':
                # sql语句
                Sql = f"select * from pyusers where username='{msg[0]}'"
                # print(Sql)
                # 使用 execute()  方法执行 SQL 语句
                try:
                    cursor.execute(Sql)
                    # 使用 fetchone() 方法获取单条数据.
                    # 使用 fetchall() 方法获取所有数据.
                    datas = cursor.fetchone()
                    if datas is None:
                        i.send('此账号不存在,登录失败!\nfalse'.encode('utf-8'))
                    elif datas[2] == msg[1]:
                        i.send('登录成功!\ntrue'.encode('utf-8'))
                    elif datas[2] != msg[1]:
                        i.send('密码错误,登录失败!\nfalse'.encode('utf-8'))
                    # 提交，不然无法保存新建或者修改的数据
                    db.commit()
                    # 关闭数据库连接
                    db.close()
                    Time = time.strftime("%Y-%m-%d %H", time.localtime())
                    # 判断记录历史客户端消息字典中当前时间key是否已存在
                    if Time in oldMessage.keys():
                        oldMessage[Time].append(msg)
                    else:
                        oldMessage[Time] = []  # 创建记录历史客户端消息的时间key
                        oldMessage[Time].append(msg)
                except Exception as MysqlExecuteError:
                    i.send('登录请求失败,请重新尝试!\nfalse'.encode('utf-8'))
                    print('MysqlExecuteError:', MysqlExecuteError)
            # 请求操作为注册
            if msg[2] == 'Register':
                # sql语句,检查此账号是否存在
                checkSql = f"select * from pyusers where username='{msg[0]}'"
                try:
                    cursor.execute(checkSql)
                    # 使用 fetchone() 方法获取单条数据.
                    # 使用 fetchall() 方法获取所有数据.
                    checkData = cursor.fetchone()
                    if checkData is None:
                        # 此账号不存在，可以注册
                        insertSql = f"insert into pyusers (username,passwd) value('{msg[0]}','{msg[1]}')"
                        # print(insertSql)
                        try:
                            if cursor.execute(insertSql):
                                i.send('注册成功!\ntrue'.encode('utf-8'))
                            else:
                                i.send('注册请求失败，请重新尝试!\nfalse'.encode('utf-8'))
                        except Exception as InsertError:
                            i.send('注册请求失败，请重新尝试!\nfalse'.encode('utf-8'))
                            print('MysqlInsertError:', InsertError)
                        # i.send('此账号不存在!\nfalse'.encode('utf-8'))
                    else:
                        # 此账号已存在，不可注册
                        i.send('此账号已存在，不可再次注册!\nfalse'.encode('utf-8'))
                    # 提交，不然无法保存新建或者修改的数据
                    db.commit()
                    # 关闭数据库连接
                    db.close()
                    Time = time.strftime("%Y-%m-%d %H", time.localtime())
                    # 判断记录历史客户端消息字典中当前时间key是否已存在
                    if Time in oldMessage.keys():
                        oldMessage[Time].append(msg)
                    else:
                        oldMessage[Time] = []  # 创建记录历史客户端消息的时间key
                        oldMessage[Time].append(msg)
                except Exception as MysqlExecuteError:
                    i.send('注册请求失败，请重新尝试!\nfalse'.encode('utf-8'))
                    print('MysqlExecuteError:', MysqlExecuteError)
        except Exception as MysqlLinkError:
            i.send('服务请求失败，请重新尝试!\nfalse'.encode('utf-8'))
            print('MysqlLinkError:', MysqlLinkError)
        finally:
            outputs.remove(i)  # outputs列表中删除该对象，如果不删除，下次循环还会误认为其发消息了
    # print(oldMessage)
