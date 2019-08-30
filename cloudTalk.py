import threading, time

# 客户端界面
from datetime import datetime

from wxPythonGUI.cloudTalk.view.cloudTalk import *

# 客户端服务
from wxPythonGUI.cloudTalk.tcp.client import clientTcp
from wxPythonGUI.cloudTalk.mysqldb.mysqldb import MysqlDb
from wx.lib.embeddedimage import PyEmbeddedImage


# 将图片的base64编码转换成bmp
def base64Img(imgbase64):
    return PyEmbeddedImage(imgbase64).GetBitmap()


global Version
Version = "v1.2"

global MainActionObj
MainActionObj = None


# 登录类
class LoginAction(LoginFrame):
    def __init__(self, parent):
        # 继承父类的构造方法
        try:
            super(LoginAction, self).__init__(parent)
        except Exception as GUIError:
            print("GUIError:", GUIError)

    # 点击Login按钮，进行登录
    def Login(self, event):
        # 获取账户和密码
        username = self.username.GetValue()
        passwd = self.passwd.GetValue()
        # 验证账户和密码
        if len(username) == 0 or len(passwd) == 0:
            wx.MessageBox("账户或密码不能为空!", "警告")
        else:
            # 将账户密码发送到服务端，登录操作
            send_data = {"username": username, "passwd": passwd, "action": "Login"}
            try:
                client = clientTcp()  # 客户端与服务端建立连接
                # 发送数据
                try:
                    resulte = client.sendData(send_data)
                    # print(resulte)
                    if resulte:
                        # wx.MessageBox('数据发送成功', '提示')
                        # 接受服务端返回的信息
                        try:
                            receive_data = client.receiveData()
                            # print(receive_data, len(receive_data), type(receive_data))
                            if len(receive_data) == 0:
                                wx.MessageBox("服务端发送数据失败!请重新尝试!", "错误")
                                # raise Exception("服务端发送数据失败!请重新尝试!")
                            else:
                                # print(receive_data)
                                wx.MessageBox(receive_data["msg"], "提示")
                                if receive_data["code"]:
                                    # 关闭登录页面
                                    self.Destroy()
                                    # 进入个人信息界面页面
                                    global MainActionObj
                                    MainActionObj = MainAction(None, username)
                                    MainActionObj.Show(True)
                                # print(receive_data)
                        except Exception as receiveError:
                            wx.MessageBox("客户端数据接收失败!请重新尝试!", "错误")
                            print("Login----receiveError:", receiveError)
                    else:
                        wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                except Exception as sendError:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                    print("sendError:", sendError)
                finally:
                    client.close()
            except Exception as linkError:
                wx.MessageBox("服务端连接失败!请重新尝试!", "错误")
                print("linkError:", linkError)

    # 点击注册按钮， 进入注册页面
    def Register(self, event):
        # 关闭登录页面
        self.Destroy()
        # 进入注册页面
        RegisterAction(None).Show(True)


# 注册类
class RegisterAction(RegisterFrame):
    def __init__(self, parent):
        # 继承父类的构造方法
        super(RegisterAction, self).__init__(parent)

    # 点击登录按钮， 进入登录页面
    def Login(self, event):
        # 关闭注册页面
        self.Destroy()
        # 进入登录页面
        LoginAction(None).Show(True)

    # 点击注册，进行注册
    def Register(self, event):
        # 获取账户和密码
        username = self.username.GetValue()
        passwd = self.passwd.GetValue()
        # 验证账户和密码的有效性
        if len(username) == 0 or len(passwd) == 0:
            wx.MessageBox("账户或密码不能为空!", "警告")
        else:
            # 将账户密码发送到服务端，注册操作
            send_data = {"username": username, "passwd": passwd, "action": "Register"}
            # send_data = username + '\n' + passwd + '\n' + 'Register'
            try:
                client = clientTcp()  # 客户端与服务端建立连接
                # 发送数据
                try:
                    resulte = client.sendData(send_data)
                    # print(resulte)
                    if resulte:
                        # wx.MessageBox('数据发送成功', '提示')
                        # 接受服务端返回的信息
                        try:
                            receive_data = client.receiveData()
                            # print(receive_data, len(receive_data), type(receive_data))
                            if len(receive_data) == 0:
                                wx.MessageBox("服务端发送数据失败!请重新尝试!", "错误")
                                # raise Exception("服务端发送数据失败!请重新尝试!")
                            else:
                                if receive_data["code"]:
                                    # 注册成功后，提示是否登陆
                                    # answer = wx.MessageBox(receive_data[0], '提示', style=wx.YES_NO)
                                    dlg = wx.MessageDialog(
                                        None,
                                        receive_data["msg"] + ",是否立即登陆?",
                                        "提示",
                                        wx.YES_NO | wx.ICON_QUESTION,
                                    )
                                    answer = dlg.ShowModal()
                                    if answer == wx.ID_YES:
                                        # print('yes')
                                        # 立即登陆，跳转到登录界面
                                        self.Login(event)
                                    elif answer == wx.ID_NO:
                                        print("no")
                                        # self.Show()
                                    dlg.Destroy()
                                    # print(retCode)
                                    # wx.MessageBox(receive_data[0], '提示')
                                else:
                                    wx.MessageBox(receive_data["msg"], "提示")
                        except Exception as receiveError:
                            wx.MessageBox("客户端数据接收失败!请重新尝试!", "错误")
                            print("Register---receiveError:", receiveError)
                    else:
                        wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                except Exception as sendError:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                    print("sendError:", sendError)
                finally:
                    client.close()
            except Exception as linkError:
                wx.MessageBox("服务端连接失败!请重新尝试!", "错误")
                print("linkError:", linkError)


# 主页面类
class MainAction(MainFrame):
    def __init__(self, parent, username):
        # 继承父类的构造方法
        super(MainAction, self).__init__(parent)
        # 获取登录成功用户的账号
        self.username = username
        # 加载主页面信息
        self.LoadInfor()
        # 登陆成功发送上线信号
        self.onlineClient = None
        self.Online()
        # 设置焦点
        self.SetFocus()

    # 加载界面信息
    def LoadInfor(self):
        db = MysqlDb()
        sql = (
            "select users.nickname,imagesicon.img_base64,users.styletext from users join imagesicon "
            "on users.username='{0}' and imagesicon.Id=users.touxiang".format(
                self.username
            )
        )
        data = db.select(sql)
        self.nickname.SetLabel("昵称:" + data[0][0])
        self.touxiang.SetBitmap(wx.NullBitmap)
        self.touxiang.SetBitmap(base64Img(data[0][1]))
        self.styletext.SetLabel("签名:" + data[0][2])
        db.close()

    #   加载联系人列表信息
    def LoadRelation(self):
        # print("username,nickname,touxiang,styletext")
        db = MysqlDb()
        sql = (
            "select users.username,users.nickname,imagesicon.img_base64,users.styletext "
            "from relations join users join imagesicon "
            "on (relations.user_1 = '{0}' or relations.user_2 = '{0}') and users.username != '{0}' "
            "and (relations.user_1 = users.username or relations.user_2 = users.username) and imagesicon.Id=users.touxiang"
            " order by users.id".format(self.username)
        )
        data = db.select(sql)
        # print(len(data))
        if data == 0:
            print("联系人列表加载失败,请重试!")
        elif len(data) > 0:
            relationsList = wx.BoxSizer(wx.VERTICAL)

            for i in range(len(data)):
                exec("fgSizer{0} = wx.FlexGridSizer(0, 2, 0, 0)".format(i))
                exec("fgSizer{0}.SetFlexibleDirection(wx.BOTH)".format(i))
                exec(
                    "fgSizer{0}.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)".format(
                        i
                    )
                )
                exec(
                    "self.touxiang{0} = wx.StaticBitmap(self.relationsArea, {0}, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,-1 ), 0)".format(
                        i
                    )
                )
                exec('self.touxiang{0}.SetToolTip(u"双击用户头像，进入聊天窗口")'.format(i))
                # 添加头像
                self.Bitmap = base64Img(data[i][2])
                exec("self.touxiang{0}.SetBitmap(self.Bitmap)".format(i))
                exec(
                    "fgSizer{0}.Add(self.touxiang{0}, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)".format(
                        i
                    )
                )
                # 绑定鼠标双击函数
                exec("self.touxiang{0}.Bind(wx.EVT_LEFT_DCLICK, self.Chat)".format(i))
                exec("usersInfor{0} = wx.BoxSizer(wx.VERTICAL)".format(i))
                exec("usersInfor{0}.SetMinSize(wx.Size(205, -1))".format(i))
                # 用户账号 ------- 隐藏性
                exec(
                    'self.user{0} = wx.TextCtrl( self.relationsArea, wx.ID_ANY, u"{1}", wx.DefaultPosition, '
                    'wx.DefaultSize, 0 )'.format(
                        i, data[i][0]
                    )
                )
                exec("self.user{0}.Hide()".format(i))
                exec("usersInfor{0}.Add(self.user{0}, 0, wx.ALL, 5)".format(i))

                exec(
                    'self.nickname{0} = wx.StaticText(self.relationsArea, wx.ID_ANY, u"昵称:{1}", wx.DefaultPosition, '
                    'wx.DefaultSize,0)'.format(
                        i, data[i][1]
                    )
                )
                exec("self.nickname{0}.Wrap(-1)".format(i))
                exec(
                    'self.nickname{0}.SetFont(wx.Font(14, 70, 90, 90, False, "微软雅黑"))'.format(
                        i
                    )
                )
                exec(
                    "usersInfor{0}.Add(self.nickname{0}, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)".format(
                        i
                    )
                )
                exec(
                    "self.z_staticline{0} = wx.StaticLine(self.relationsArea, wx.ID_ANY, wx.DefaultPosition, "
                    "wx.DefaultSize,wx.LI_HORIZONTAL)".format(
                        i
                    )
                )
                exec(
                    "usersInfor{0}.Add(self.z_staticline{0}, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)".format(
                        i
                    )
                )
                exec(
                    'self.styletext{0} = wx.StaticText(self.relationsArea, wx.ID_ANY, u"签名:{1}", wx.DefaultPosition,'
                    "wx.DefaultSize, 0)".format(i, data[i][3])
                )
                exec("self.styletext{0}.Wrap(-1)".format(i))
                exec(
                    'self.styletext{0}.SetFont(wx.Font(12, 70, 90, 90, False, "微软雅黑"))'.format(
                        i
                    )
                )
                exec(
                    "usersInfor{0}.Add(self.styletext{0}, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)".format(
                        i
                    )
                )
                exec(
                    "fgSizer{0}.Add(usersInfor{0}, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | "
                    "wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)".format(
                        i
                    )
                )
                exec("relationsList.Add(fgSizer{0}, 0, wx.EXPAND, 5)".format(i))
                exec(
                    "self.m_staticline{0} = wx.StaticLine(self.relationsArea, wx.ID_ANY, wx.DefaultPosition, "
                    "wx.DefaultSize,wx.LI_HORIZONTAL)".format(i)
                )
                exec(
                    "relationsList.Add(self.m_staticline{0}, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL,5)".format(
                        i
                    )
                )

            self.relationsArea.SetSizer(relationsList)
            self.relationsArea.Layout()
            relationsList.Fit(self.relationsArea)
            # print(data)
        db.close()

    #  上线后开启多线程
    def Online(self):
        try:
            self.onlineClient = clientTcp(port=11112)
            try:
                global Version
                result = self.onlineClient.sendData(
                    {"username": self.username, "action": "Online", "Version": Version}
                )
                if not result:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                    self.onlineClient.close()
                    self.Online()
                else:
                    # 开启在线接收数据任务线程
                    Receiv = threading.Thread(target=self.ReceiveData)
                    Receiv.setDaemon(True)
                    Receiv.start()
            except Exception as sendError:
                wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                print("sendError:", sendError)
                self.onlineClient.close()
                self.Online()
        except Exception as linkError:
            wx.MessageBox("服务端连接失败!请重新尝试!", "错误")
            print("linkError:", linkError)
            self.Online()

    # 发送心跳信号
    def Ping(self):
        timer = threading.Timer(50, self.Ping)
        if not self.onlineClient == None:
            result = self.onlineClient.sendData({"action": "Ping"})
            timer.start()

    # 主界面退出时
    def MainClose(self, event):
        # print('线程数量：',threading.activeCount())
        dlg = wx.MessageDialog(
            self, '请确定是否退出"云上畅谈"?', "提示", style=wx.YES_NO | wx.ICON_QUESTION
        )
        answer = dlg.ShowModal()
        if answer == wx.ID_YES:
            # 告知服务端下线，给当前正在与自己的聊天好友们 发送下线消息
            self.onlineClient.sendData({"action": "Close"})
            self.onlineClient = None
            global ChatUserFrame
            for key in ChatUserFrame:
                # 关闭所有聊天窗口
                ChatUserFrame[key].Destroy()
            # 删除
            del ChatUserFrame
            self.Destroy()
        # print('线程数量：', threading.activeCount())
        dlg.Destroy()

    def EscDown(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self.MainClose(None)

    # 接收从服务端来数据
    def ReceiveData(self):
        # 开始发送心跳
        threading.Timer(50, self.Ping).start()
        while not self.onlineClient == None:
            try:
                receive_data = self.onlineClient.receiveData()
                if len(receive_data) == 0:
                    wx.MessageBox("服务端发送数据失败!请重新尝试!", "错误")
                else:
                    try:
                        if type(receive_data) == list:
                            # 处理自己未上线前的临时存储消息
                            self.TempInforsProcess(receive_data)
                        elif type(receive_data) == dict:
                            self.ProcessData(receive_data)
                    except Exception as processError:
                        print("processData--processError:", processError)
            except Exception as receiveError:
                print("ReceiveData--receiveError:", receiveError, type(receiveError))
                if type(receiveError) == ConnectionResetError:
                    wx.MessageBox("客户端与服务器已断开,请重新登陆!", "错误")
                    self.Destroy()
                wx.MessageBox("客户端数据接收失败!请重新尝试!", "错误")
                # print('ReceiveData--receiveError:', receiveError)

    def TempInforsProcess(self, data):
        for i in range(len(data)):
            # 再将根本信息数据传递，交由请求处理函数
            self.ProcessData(data[i][1])
            # 暂停2秒，避免一次性产生多个请求，影响使用体验
            time.sleep(3)

    # 处理接收的数据，处理请求
    def ProcessData(self, data):
        # 显示所搜索的其他用户信息
        if data["action"] == "Search" and data["code"]:
            infors = data["msg"]
            newData = {
                "otherUser": infors["username"],
                "nickname": infors["nickname"],
                "client": self.onlineClient,
            }
            wx.CallAfter(self.OtherUser, newData)
        # 显示发起好友添加请求的用户信息
        elif data["action"] == "SearchAdd" and data["code"]:
            # print(data)
            data = {
                "otherUser": data["otherUser"]["username"],
                "nickname": data["otherUser"]["nickname"],
                "alertTitle": data["msg"],
                "client": self.onlineClient,
            }
            wx.CallAfter(self.OtherUser, data)
        # 目前处于在线中，对方同意了你的添加请求，实时重载联系人列表
        elif data["action"] == "AddAgree" and data["code"]:
            wx.CallAfter(self.LoadRelation)
            wx.MessageBox(data["msg"], "提示")
        # 刚上线情况，或者刚同意了对方的申请，重载联系人列表
        elif data["action"] == "Online" and data["code"]:
            wx.CallAfter(self.LoadRelation)
        # 显示当前聊天窗口的对方是否在线
        elif data["action"] == "sureOnline":
            global ChatUserFrame
            # 给当前某个用户窗口，提示是否在线信息
            if data["otherUser"] in ChatUserFrame:
                if not data["code"]:
                    # 声明类时得到的返回值，调用类里的函数，来改变label值
                    ChatUserFrame[data["otherUser"]].changeInfor(" 离线")
                else:
                    ChatUserFrame[data["otherUser"]].changeInfor(" 在线")
        elif data["action"] == "Chat" and data["code"]:
            # 进入主线程，调用
            wx.CallAfter(self.ChatInforsShow, data)
        elif data["action"] == "Version" and data["code"]:
            # 提示版本更新
            wx.MessageBox(data["msg"], "提示")
            self.Destroy()
        elif data["action"] == "Ping":
            print(data)
        else:
            wx.MessageBox(data["msg"], "提示")

    # 通讯功能  点击用户头像
    def Chat(self, event):
        id = event.GetId()
        exec(
            "self.chatFrame(self.user{0}.GetValue(),self.nickname{0}.GetLabel())".format(
                id
            )
        )

    # 防止对同一个用户创建多个同样聊天窗口
    global ChatUserFrame
    ChatUserFrame = {}

    def chatFrame(self, otherusername, othernickname):
        global ChatUserFrame
        if otherusername in ChatUserFrame:
            print(otherusername, "已经点击过")
        else:
            ChatUserFrame[otherusername] = ChatAction(
                None,
                otherusername,
                othernickname,
                self.onlineClient,
                self.nickname.GetLabel(),
            )
            ChatUserFrame[otherusername].Show(True)
            self.onlineClient.sendData(
                {"action": "sureOnline", "otherUser": otherusername}
            )

    def ChatInforsShow(self, data):
        global ChatUserFrame
        # 窗口还未打开，则创建
        if not (data["otherUser"] in ChatUserFrame):
            self.chatFrame(data["otherUser"], data["nickname"])
        # 添加聊天信息
        ChatUserFrame[data["otherUser"]].changeChatInfor(data["msg"])
        # # 获取焦点
        # ChatUserFrame[data['otherUser']].SetTopWindow(self)
        # WinAPI:SetWindowPos(ChatUserFrame[data['otherUser']],0)

    # 查询指定用户----点击查询
    def SearchBtn(self, event):
        otherUsers = self.search.GetValue()
        if len(otherUsers) == 0:
            wx.MessageBox("查询账号不能为空！", "提示")
        else:
            # 查询用户自己，进入用户个人信息界面
            if otherUsers == self.username:
                global UserInforBool
                if not UserInforBool:
                    self.UserInfor(None)
            else:
                try:
                    global OtherUserList
                    OtherUserList.index(otherUsers)
                except:
                    try:
                        result = self.onlineClient.sendData(
                            {"otherUser": otherUsers, "action": "Search"}
                        )
                        if not result:
                            wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                    except Exception as sendError:
                        wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
                        print("sendError:", sendError)

    # 显示用户个人信息
    global UserInforBool
    UserInforBool = False

    def UserInfor(self, event):
        global UserInforBool
        if not UserInforBool:
            # 开启界面条件
            UserInforBool = True
            UserInforAction(self, self.username).Show(True)

    # 显示搜索的用户信息
    global OtherUserList
    OtherUserList = []

    def OtherUser(self, data):
        if len(data) == 3:
            global OtherUserList
            OtherUserList.append(data["otherUser"])
            AddUserAction(self, data=data).Show()
        elif len(data) == 4:
            AddUserAction(self, data=data).Show()

    # 使用手册界面信息
    # 禁止创建多个手册界面
    global IntroBool
    IntroBool = False

    def EnterIntro(self, event):
        global IntroBool
        if not IntroBool:
            # 开启禁止创建界面条件
            IntroBool = True
            IntroAction(self).Show(True)


# 用户个人信息类
class UserInforAction(UserInforFrame):
    def __init__(self, parent, username):
        # 继承父类的构造方法
        super(UserInforAction, self).__init__(parent)
        self.initInfor(username)

    def initInfor(self, username):
        db = MysqlDb()
        sql = (
            "select users.username,users.nickname,users.register_time,imagesicon.img_base64,users.styletext "
            "from users join imagesicon "
            "on users.username='{0}' and imagesicon.Id=users.touxiang".format(username)
        )
        data = db.select(sql)
        self.childUsername.SetValue(data[0][0])
        self.childNickname.SetValue(data[0][1])
        self.register_time.SetValue(data[0][2].strftime("%Y-%m-%d %H:%M:%S"))
        self.childTouxiang.SetBitmap(base64Img(data[0][3]))
        self.childStyletext.SetValue(data[0][4])
        db.close()

    # 修改保存个人信息
    def saveUserInfor(self, event):
        if not self.childNickname.GetValue() == "我是管理员":
            db = MysqlDb()
            sql = "UPDATE users SET nickname = '{0}',styletext = '{1}' WHERE username = '{2}'".format(
                self.childNickname.GetValue(),
                self.childStyletext.GetValue(),
                self.childUsername.GetValue(),
            )
            print(sql)
            data = db.update(sql)
            db.close()
            if data:
                wx.MessageBox("保存成功", "提示")
                # 改变父界面的个人简要信息
                global MainActionObj
                MainActionObj.LoadInfor()
            else:
                wx.MessageBox("保存失败,请重新尝试!", "提示")
        else:
            wx.MessageBox('个人昵称不能设置成"我是管理员",请更改!', "提示")

    # 关闭界面
    def UserInforClose(self, event):
        global UserInforBool
        # 重置界面开启条件
        UserInforBool = False
        self.Destroy()


# 添加或被添加用户相关的操作类
class AddUserAction(AddUserInfor):
    def __init__(self, parent, data=None):
        # 继承父类的构造方法
        # print(data)
        try:
            super(AddUserAction, self).__init__(parent)
            self.data = data
            self.childUsername.SetValue(self.data["otherUser"])
            nickname = "无" if self.data["nickname"] == None else self.data["nickname"]
            self.childNickname.SetValue(nickname)
            self.dataLen = len(self.data)
            if self.dataLen == 4:
                self.alertTitle.SetLabel(self.data["alertTitle"])
        except Exception as eroor:
            print("error:", eroor)

    # 发送好友添加请求或同意好友添加
    def SearchAdd(self, event):
        onlineClient = self.data["client"]
        try:
            # 同意好友添加
            if self.dataLen == 4:
                result = onlineClient.sendData(
                    {
                        "otherUser": self.data["otherUser"],
                        "code": 1,
                        "action": "AddAgree",
                    }
                )
                if not result:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
            # 发起好友添加请求
            else:
                result = onlineClient.sendData(
                    {"otherUser": self.data["otherUser"], "action": "SearchAdd"}
                )
                if not result:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
        except Exception as sendError:
            wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
            print("sendError:", sendError)
        finally:
            if self.dataLen == 3:
                global OtherUserList
                # 发起添加信号后，移除当前搜索的用户username
                OtherUserList.remove(self.data["otherUser"])
            self.Destroy()

    # 关闭搜索窗口或拒绝好友添加
    def SearchClose(self, event):
        onlineClient = self.data["client"]
        # 不同意好友添加
        try:
            if self.dataLen == 4:
                result = onlineClient.sendData(
                    {
                        "otherUser": self.data["otherUser"],
                        "code": 0,
                        "action": "AddAgree",
                    }
                )
                if not result:
                    wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
        except Exception as sendError:
            wx.MessageBox("客户端数据发送失败!请重新尝试!", "错误")
            print("sendError:", sendError)
        finally:
            if self.dataLen == 3:
                global OtherUserList
                # 关闭搜索移除当前搜索的用户username
                OtherUserList.remove(self.data["otherUser"])
            self.Destroy()


# 聊天界面类
class ChatAction(ChatFrame):
    # 父窗口 对方账号，昵称 ，tcp套接字，自己昵称
    def __init__(self, parent, otherusername, othernickname, onlineClient, nickname):
        # 继承父类的构造方法
        super(ChatAction, self).__init__(parent)
        # 对方账号
        self.otherusername = otherusername
        # tcp套接字
        self.onlineClient = onlineClient
        # 加载界面信息
        self.initLoadInfor(othernickname)
        # 自己的昵称
        self.nickname = nickname

    def initLoadInfor(self, othernickname):
        # self.otherUser.SetLabel(self.otherusername)
        self.othernickname.SetLabel(othernickname)
        self.SetFocus()

    # 改变在线信息
    def changeInfor(self, online):
        self.isOnline.SetLabel(online)

    # 改变聊天信息
    def changeChatInfor(self, data):
        self.showData.AppendText(data)

    def SendData(self, event):
        data = self.inputinfors.GetValue()
        print(data, type(data), len(data))
        self.inputinfors.Clear()
        if not data == "" and not data == "\n" and len(data) > 0:
            data = (
                    self.nickname
                    + " "
                    + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    + "\n"
                    + data
                    + "\n"
            )
            # 发送聊天消息
            self.onlineClient.sendData(
                # 指令 发送数据 接收方账号 自己昵称
                {
                    "action": "Chat",
                    "infors": data,
                    "otherUser": self.otherusername,
                    "nickname": self.nickname,
                }
            )
            self.showData.AppendText(data)
        else:
            wx.MessageBox("发送内容不能为空!", "提示")
            self.inputinfors.Clear()

    def getFocus(self, event):
        # self.SetCursor(wxCursor(wxCURSOR_WAIT))
        # self.SetFocus()
        data = self.inputinfors.GetValue()
        if data == "输入点什么吧....":
            self.inputinfors.SetValue("")
        elif not data == "输入点什么吧....":
            self.inputinfors.SetValue(data)

    def killFocus(self, event):
        data = self.inputinfors.GetValue()
        if data == "":
            self.inputinfors.SetValue("输入点什么吧....")
        elif not data == "":
            self.inputinfors.SetValue(data)

    def ChatClose(self, event):
        global ChatUserFrame
        dlg = wx.MessageDialog(
            ChatUserFrame[self.otherusername],
            "是否退出聊天界面？",
            "提示",
            wx.YES_NO | wx.ICON_QUESTION,
        )
        answer = dlg.ShowModal()
        if answer == wx.ID_YES:
            self.Destroy()
            del ChatUserFrame[self.otherusername]

    # 按下esc
    def keyDown(self, event):
        key = event.GetKeyCode()
        # print(key)
        if key == wx.WXK_ESCAPE:
            self.ChatClose(None)

    # 双击用户昵称 进入对方用户信息界面
    def otherUserInfor(self, event):
        global OtherUserInforDict
        if not (self.otherusername in OtherUserInforDict):
            OtherUserInforDict[self.otherusername] = OtherUserInforAction(
                self, self.otherusername
            )
            OtherUserInforDict[self.otherusername].Show(True)
            print(OtherUserInforDict)


# 云上畅谈平台使用说明类
class IntroAction(introductionFrame):
    def __init__(self, parent):
        # 继承父类的构造方法
        super(IntroAction, self).__init__(parent)

    def introClose(self, event):
        global IntroBool
        # 关闭界面 重置界面创建条件
        IntroBool = False
        self.Destroy()


# 防止多次点击 多开bug
global OtherUserInforDict
OtherUserInforDict = {}


# 其他用户信息界面
class OtherUserInforAction(OtherUserInforFrame):
    def __init__(self, parent, otheruser):
        # 继承父类的构造方法
        super(OtherUserInforAction, self).__init__(parent)
        self.otheruser = otheruser
        self.initInfor()

    def initInfor(self):
        db = MysqlDb()
        sql = (
            "select users.username,users.nickname,imagesicon.img_base64,users.styletext "
            "from users join imagesicon "
            "on users.username='{0}' and imagesicon.Id=users.touxiang".format(
                self.otheruser
            )
        )
        data = db.select(sql)
        self.childUsername.SetValue(data[0][0])
        self.childNickname.SetValue(data[0][1])
        self.childTouxiang.SetBitmap(base64Img(data[0][2]))
        self.childStyletext.SetValue(data[0][3])
        db.close()

    def otherUserInforClose(self, event):
        global OtherUserInforDict
        # 关闭界面 重置界面创建条件
        del OtherUserInforDict[self.otheruser]
        print(OtherUserInforDict)
        self.Destroy()


app = wx.App(False)
frame = LoginAction(None)
frame.Show(True)
app.MainLoop()
