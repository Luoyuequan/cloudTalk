# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

login_1 = 1000
register_1 = 1001

###########################################################################
## Class LoginFrame
###########################################################################


class LoginFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(-1, -1),
            style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_NO_TASKBAR | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)

        all = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(
            self,
            wx.ID_ANY,
            u"用户登录",
            wx.Point(-1, -1),
            wx.Size(-1, -1),
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.title.Wrap(-1)

        self.title.SetFont(
            wx.Font(
                40,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "隶书",
            )
        )
        self.title.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT)
        )
        self.title.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE)
        )

        all.Add(self.title, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.LoginPanelArea = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        self.LoginPanelArea.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE)
        )

        LoginMainArea = wx.BoxSizer(wx.VERTICAL)

        userInput = wx.FlexGridSizer(0, 2, 0, 0)
        userInput.SetFlexibleDirection(wx.BOTH)
        userInput.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.userText = wx.StaticText(
            self.LoginPanelArea,
            wx.ID_ANY,
            u"账号:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.userText.Wrap(-1)

        self.userText.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        userInput.Add(
            self.userText,
            0,
            wx.ALIGN_CENTER_VERTICAL
            | wx.TOP
            | wx.BOTTOM
            | wx.LEFT
            | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.username = wx.TextCtrl(
            self.LoginPanelArea,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(200, -1),
            wx.TE_PROCESS_ENTER,
        )
        self.username.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.username.SetToolTip(u"请输入账号")

        userInput.Add(
            self.username,
            0,
            wx.TOP
            | wx.BOTTOM
            | wx.RIGHT
            | wx.ALIGN_CENTER_HORIZONTAL
            | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.passwdText = wx.StaticText(
            self.LoginPanelArea,
            wx.ID_ANY,
            u"密码:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.passwdText.Wrap(-1)

        self.passwdText.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        userInput.Add(
            self.passwdText,
            0,
            wx.ALIGN_CENTER_VERTICAL
            | wx.TOP
            | wx.BOTTOM
            | wx.LEFT
            | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.passwd = wx.TextCtrl(
            self.LoginPanelArea,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(200, -1),
            wx.TE_PASSWORD | wx.TE_PROCESS_ENTER,
        )
        self.passwd.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.passwd.SetToolTip(u"请输入密码")

        userInput.Add(
            self.passwd,
            0,
            wx.ALIGN_CENTER_HORIZONTAL
            | wx.TOP
            | wx.BOTTOM
            | wx.RIGHT
            | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        LoginMainArea.Add(userInput, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        LoginBtn = wx.FlexGridSizer(0, 2, 0, 0)
        LoginBtn.SetFlexibleDirection(wx.BOTH)
        LoginBtn.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.login = wx.Button(
            self.LoginPanelArea, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.login.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.login.SetToolTip(u"登录")

        LoginBtn.Add(
            self.login, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5
        )

        self.register = wx.Button(
            self.LoginPanelArea,
            wx.ID_ANY,
            u"注册→",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.register.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.register.SetToolTip(u"跳转到注册界面")

        LoginBtn.Add(
            self.register,
            0,
            wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        LoginMainArea.Add(LoginBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.LoginPanelArea.SetSizer(LoginMainArea)
        self.LoginPanelArea.Layout()
        LoginMainArea.Fit(self.LoginPanelArea)
        all.Add(self.LoginPanelArea, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(all)
        self.Layout()
        all.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.username.Bind(wx.EVT_TEXT_ENTER, self.Login)
        self.passwd.Bind(wx.EVT_TEXT_ENTER, self.Login)
        self.login.Bind(wx.EVT_BUTTON, self.Login)
        self.register.Bind(wx.EVT_BUTTON, self.Register)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def Login(self, event):
        event.Skip()

    def Register(self, event):
        event.Skip()


###########################################################################
## Class RegisterFrame
###########################################################################


class RegisterFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(-1, -1),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)

        all = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(
            self,
            wx.ID_ANY,
            u"用户注册",
            wx.Point(-1, -1),
            wx.Size(-1, -1),
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.title.Wrap(-1)

        self.title.SetFont(
            wx.Font(
                40,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "隶书",
            )
        )
        self.title.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT)
        )
        self.title.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE)
        )

        all.Add(self.title, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_panel4 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        self.m_panel4.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE)
        )

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        nameArea = wx.FlexGridSizer(0, 2, 0, 0)
        nameArea.SetFlexibleDirection(wx.BOTH)
        nameArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.userText = wx.StaticText(
            self.m_panel4, wx.ID_ANY, u"*账号:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.userText.Wrap(-1)

        self.userText.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.userText.SetForegroundColour(wx.Colour(255, 0, 0))

        nameArea.Add(
            self.userText,
            0,
            wx.ALIGN_CENTER_VERTICAL
            | wx.TOP
            | wx.BOTTOM
            | wx.LEFT
            | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.username = wx.TextCtrl(
            self.m_panel4,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(200, -1),
            wx.TE_PROCESS_ENTER,
        )
        self.username.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.username.SetToolTip(u"请输入账号")

        nameArea.Add(
            self.username,
            0,
            wx.ALIGN_CENTER_HORIZONTAL
            | wx.ALIGN_CENTER_VERTICAL
            | wx.TOP
            | wx.BOTTOM
            | wx.RIGHT,
            5,
        )

        bSizer17.Add(
            nameArea, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5
        )

        passwdArea = wx.FlexGridSizer(0, 2, 0, 0)
        passwdArea.SetFlexibleDirection(wx.BOTH)
        passwdArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.passwdText = wx.StaticText(
            self.m_panel4, wx.ID_ANY, u"*密码:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.passwdText.Wrap(-1)

        self.passwdText.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.passwdText.SetForegroundColour(wx.Colour(255, 0, 0))

        passwdArea.Add(
            self.passwdText,
            1,
            wx.ALIGN_CENTER_VERTICAL
            | wx.TOP
            | wx.BOTTOM
            | wx.LEFT
            | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.passwd = wx.TextCtrl(
            self.m_panel4,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(200, -1),
            wx.TE_PASSWORD | wx.TE_PROCESS_ENTER,
        )
        self.passwd.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.passwd.SetToolTip(u"请输入密码")

        passwdArea.Add(
            self.passwd,
            0,
            wx.ALIGN_CENTER_HORIZONTAL
            | wx.TOP
            | wx.BOTTOM
            | wx.RIGHT
            | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        bSizer17.Add(
            passwdArea,
            0,
            wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.RIGHT | wx.LEFT,
            5,
        )

        userBtn = wx.GridSizer(0, 2, 0, 0)

        self.login = wx.Button(
            self.m_panel4, login_1, u"←登录", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.login.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.login.SetToolTip(u"跳转到登录界面")

        userBtn.Add(
            self.login,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.register = wx.Button(
            self.m_panel4, register_1, u"注册", wx.DefaultPosition, wx.Size(-1, -1), 0
        )
        self.register.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "楷体",
            )
        )
        self.register.SetToolTip(u"注册")

        userBtn.Add(
            self.register,
            0,
            wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        bSizer17.Add(userBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer17)
        self.m_panel4.Layout()
        bSizer17.Fit(self.m_panel4)
        all.Add(self.m_panel4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(all)
        self.Layout()
        all.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.username.Bind(wx.EVT_TEXT_ENTER, self.Register)
        self.passwd.Bind(wx.EVT_TEXT_ENTER, self.Register)
        self.login.Bind(wx.EVT_BUTTON, self.Login)
        self.register.Bind(wx.EVT_BUTTON, self.Register)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def Register(self, event):
        event.Skip()

    def Login(self, event):
        event.Skip()


###########################################################################
## Class MainFrame
###########################################################################


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(310, 690),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(310, 690), wx.Size(310, 690))
        self.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )

        all = wx.BoxSizer(wx.VERTICAL)

        HeaderArea = wx.FlexGridSizer(0, 2, 0, 0)
        HeaderArea.SetFlexibleDirection(wx.BOTH)
        HeaderArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.touxiang = wx.StaticBitmap(
            self, wx.ID_ANY, wx.NullBitmap, wx.Point(-1, -1), wx.Size(48, 48), 0
        )
        self.touxiang.SetToolTip(u"双击个人头像，显示个人信息界面")

        HeaderArea.Add(
            self.touxiang,
            0,
            wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        usersInfor = wx.BoxSizer(wx.VERTICAL)

        usersInfor.SetMinSize(wx.Size(240, -1))
        self.nickname = wx.StaticText(
            self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.nickname.Wrap(-1)

        self.nickname.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "微软雅黑",
            )
        )
        self.nickname.SetToolTip(u"编辑昵称，请进入个人信息界面")

        usersInfor.Add(
            self.nickname,
            0,
            wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.RIGHT | wx.LEFT,
            5,
        )

        self.m_staticline22 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        self.m_staticline22.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        )
        self.m_staticline22.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        )

        usersInfor.Add(
            self.m_staticline22, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.styletext = wx.StaticText(
            self, wx.ID_ANY, u"个性签名", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.styletext.Wrap(-1)

        self.styletext.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.styletext.SetToolTip(u"编辑个性签名，请进入个人信息界面")

        usersInfor.Add(
            self.styletext,
            0,
            wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT,
            5,
        )

        HeaderArea.Add(usersInfor, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        all.Add(HeaderArea, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.search = wx.SearchCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_PROCESS_ENTER,
        )
        self.search.ShowSearchButton(True)
        self.search.ShowCancelButton(True)
        self.search.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "微软雅黑",
            )
        )
        self.search.SetToolTip(u"请输入需要查询的账号")

        all.Add(
            self.search,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND,
            5,
        )

        self.InforArea = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH
        )
        self.messageArea = wx.ScrolledWindow(
            self.InforArea,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.HSCROLL | wx.VSCROLL,
        )
        self.messageArea.SetScrollRate(5, 5)
        messageList = wx.BoxSizer(wx.VERTICAL)

        self.intro_text = wx.StaticText(
            self.messageArea,
            wx.ID_ANY,
            u"云上畅谈 使用介绍,初次使用者必看!",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.intro_text.Wrap(-1)

        self.intro_text.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "微软雅黑",
            )
        )

        messageList.Add(
            self.intro_text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.ALL, 5
        )

        self.intro_btn = wx.Button(
            self.messageArea,
            wx.ID_ANY,
            u"详情点击进入",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        messageList.Add(
            self.intro_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5
        )

        self.m_staticline21 = wx.StaticLine(
            self.messageArea,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LI_HORIZONTAL,
        )
        messageList.Add(
            self.m_staticline21, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.messageArea.SetSizer(messageList)
        self.messageArea.Layout()
        messageList.Fit(self.messageArea)
        self.InforArea.AddPage(self.messageArea, u"消息", True)
        self.relationsArea = wx.ScrolledWindow(
            self.InforArea,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.HSCROLL | wx.VSCROLL,
        )
        self.relationsArea.SetScrollRate(5, 5)
        self.InforArea.AddPage(self.relationsArea, u"联系人", False)
        self.dynamicArea = wx.ScrolledWindow(
            self.InforArea,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.HSCROLL | wx.VSCROLL,
        )
        self.dynamicArea.SetScrollRate(5, 5)
        dynamicList = wx.BoxSizer(wx.VERTICAL)

        self.dynamicArea.SetSizer(dynamicList)
        self.dynamicArea.Layout()
        dynamicList.Fit(self.dynamicArea)
        self.InforArea.AddPage(self.dynamicArea, u"动态", False)

        all.Add(self.InforArea, 1, wx.EXPAND, 5)

        self.SetSizer(all)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.MainClose)
        self.Bind(wx.EVT_KEY_DOWN, self.EscDown)
        self.touxiang.Bind(wx.EVT_LEFT_DCLICK, self.UserInfor)
        self.search.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.SearchBtn)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.SearchBtn)
        self.intro_btn.Bind(wx.EVT_BUTTON, self.EnterIntro)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def MainClose(self, event):
        event.Skip()

    def EscDown(self, event):
        event.Skip()

    def UserInfor(self, event):
        event.Skip()

    def SearchBtn(self, event):
        event.Skip()

    def EnterIntro(self, event):
        event.Skip()


###########################################################################
## Class UserInforFrame
###########################################################################


class UserInforFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(460, 370),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(460, 370), wx.DefaultSize)

        All = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(
            self, wx.ID_ANY, u"用户个人信息", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(
            wx.Font(
                30,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        All.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.childTouxiang = wx.StaticBitmap(
            self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(60, 60), 0
        )
        All.Add(self.childTouxiang, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        InforArea = wx.FlexGridSizer(0, 2, 0, 0)
        InforArea.SetFlexibleDirection(wx.BOTH)
        InforArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText14 = wx.StaticText(
            self, wx.ID_ANY, u"用户账号", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.m_staticText14,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childUsername = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(300, -1),
            wx.TE_READONLY,
        )
        self.childUsername.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childUsername,
            1,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT | wx.EXPAND,
            5,
        )

        self.m_staticText15 = wx.StaticText(
            self, wx.ID_ANY, u"用户昵称", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.m_staticText15,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childNickname = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0
        )
        self.childNickname.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childNickname,
            1,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT | wx.EXPAND,
            5,
        )

        self.m_staticText151 = wx.StaticText(
            self, wx.ID_ANY, u"注册时间", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText151.Wrap(-1)

        self.m_staticText151.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.m_staticText151,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.register_time = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.TE_READONLY,
        )
        self.register_time.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.register_time,
            1,
            wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.m_staticText1511 = wx.StaticText(
            self, wx.ID_ANY, u"个性签名", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText1511.Wrap(-1)

        self.m_staticText1511.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(self.m_staticText1511, 0, wx.ALL, 5)

        self.childStyletext = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0
        )
        self.childStyletext.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childStyletext,
            1,
            wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        All.Add(InforArea, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.save = wx.Button(
            self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.save.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        All.Add(self.save, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(All)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.UserInforClose)
        self.save.Bind(wx.EVT_BUTTON, self.saveUserInfor)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def UserInforClose(self, event):
        event.Skip()

    def saveUserInfor(self, event):
        event.Skip()


###########################################################################
## Class introductionFrame
###########################################################################


class introductionFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(500, 400),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(500, 400), wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER)
        )

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.intro_title = wx.StaticText(
            self, wx.ID_ANY, u"使用手册", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.intro_title.Wrap(-1)

        self.intro_title.SetFont(
            wx.Font(
                30,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文行楷",
            )
        )

        bSizer9.Add(self.intro_title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline7 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        bSizer9.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText15 = wx.StaticText(
            self,
            wx.ID_ANY,
            u"亲爱的用户，您好！感谢你使用本产品。\n本产品目前具有如下功能：\n1.添加好友，通过主界面的查询栏，输入对方云账号，点击查询按钮，即可看见对方简要信息，点击添加按钮即可添加。\n2.好友聊天，选择你聊天的好友，双击好友头像，即可进入聊天界面，然后你就可以与你的好友进行畅谈。\n最后再次感谢你使用本产品，希望你继续支持我们，让我们对此产品做更好的优化。\n如有疑问或建议，可将你的内容发送至这个电子邮箱:1260612638@qq.com。\n软件下载地址:www.luoyuequan.cn",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "华文新魏",
            )
        )
        self.m_staticText15.Hide()

        bSizer9.Add(self.m_staticText15, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl14 = wx.TextCtrl(
            self,
            wx.ID_ANY,
            u"亲爱的用户，您好！感谢你使用本产品。\n本产品目前具有如下功能：\n1.添加好友，通过主界面的查询栏，输入对方云账号，点击查询按钮，即可看见对方简要信息，点击添加按钮即可添加。\n2.好友聊天，选择你聊天的好友，双击好友头像，即可进入聊天界面，然后你就可以与你的好友进行畅谈。\n最后再次感谢你使用本产品，希望你继续支持我们，让我们对此产品做更好的优化。\n如有疑问或建议，可将你的内容发送至这个电子邮箱:1260612638@qq.com。\n软件下载地址:www.luoyuequan.cn",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE | wx.TE_NO_VSCROLL | wx.TE_READONLY | wx.BORDER_NONE,
        )
        self.m_textCtrl14.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "华文新魏",
            )
        )
        self.m_textCtrl14.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER)
        )

        bSizer9.Add(self.m_textCtrl14, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.introClose)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def introClose(self, event):
        event.Skip()


###########################################################################
## Class AddUserInfor
###########################################################################


class AddUserInfor(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"搜索好友",
            pos=wx.DefaultPosition,
            size=wx.Size(400, 300),
            style=wx.CAPTION,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(
            self, wx.ID_ANY, u"用户信息", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(
            wx.Font(
                30,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        bSizer9.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer6 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText14 = wx.StaticText(
            self, wx.ID_ANY, u"用户账号", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer6.Add(
            self.m_staticText14,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childUsername = wx.TextCtrl(
            self,
            wx.ID_ANY,
            u"None",
            wx.DefaultPosition,
            wx.Size(200, -1),
            wx.TE_READONLY,
        )
        self.childUsername.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer6.Add(
            self.childUsername,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT | wx.EXPAND,
            5,
        )

        self.m_staticText15 = wx.StaticText(
            self, wx.ID_ANY, u"用户昵称", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer6.Add(
            self.m_staticText15,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childNickname = wx.TextCtrl(
            self,
            wx.ID_ANY,
            u"None",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.TE_READONLY,
        )
        self.childNickname.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer6.Add(
            self.childNickname,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        bSizer9.Add(fgSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.alertTitle = wx.StaticText(
            self, wx.ID_ANY, u"是否将对方添加为好友？", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.alertTitle.Wrap(-1)

        self.alertTitle.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        bSizer9.Add(self.alertTitle, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer10 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.AddBtn = wx.Button(
            self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.AddBtn.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer10.Add(self.AddBtn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.CloseBtn = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.CloseBtn.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        fgSizer10.Add(
            self.CloseBtn,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        bSizer9.Add(fgSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_KEY_DOWN, self.lll)
        self.AddBtn.Bind(wx.EVT_BUTTON, self.SearchAdd)
        self.CloseBtn.Bind(wx.EVT_BUTTON, self.SearchClose)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def lll(self, event):
        event.Skip()

    def SearchAdd(self, event):
        event.Skip()

    def SearchClose(self, event):
        event.Skip()


###########################################################################
## Class ChatFrame
###########################################################################


class ChatFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(600, 600),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(500, 500), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        allbox = wx.BoxSizer(wx.VERTICAL)

        fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.othernickname = wx.StaticText(
            self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.othernickname.Wrap(-1)

        self.othernickname.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "楷体",
            )
        )
        self.othernickname.SetToolTip(u"双击进入用户信息界面")

        fgSizer9.Add(
            self.othernickname, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5
        )

        self.isOnline = wx.StaticText(
            self, wx.ID_ANY, u"是否在线", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.isOnline.Wrap(-1)

        self.isOnline.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "楷体",
            )
        )
        self.isOnline.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT)
        )

        fgSizer9.Add(self.isOnline, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        allbox.Add(fgSizer9, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        mainChat = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"聊天消息显示区域"), wx.VERTICAL
        )

        self.showData = wx.TextCtrl(
            mainChat.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_NONE,
        )
        self.showData.SetFont(
            wx.Font(
                11,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_LIGHT,
                False,
                "黑体",
            )
        )
        self.showData.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU)
        )

        mainChat.Add(self.showData, 1, wx.EXPAND, 2)

        allbox.Add(mainChat, 1, wx.EXPAND, 5)

        inputbox = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"聊天输入区域"), wx.VERTICAL
        )

        self.inputinfors = wx.TextCtrl(
            inputbox.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.TE_MULTILINE | wx.TE_PROCESS_ENTER,
        )
        self.inputinfors.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "楷体",
            )
        )
        self.inputinfors.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        )
        self.inputinfors.SetToolTip(u"输入点什么吧.....\n按下Enter键发送\n或者点击发送按钮")

        inputbox.Add(self.inputinfors, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.sendbtn = wx.Button(
            inputbox.GetStaticBox(),
            wx.ID_ANY,
            u"发送",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.sendbtn.SetFont(
            wx.Font(
                14,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "楷体",
            )
        )

        inputbox.Add(self.sendbtn, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        allbox.Add(inputbox, 1, wx.EXPAND, 5)

        self.otherUser = wx.StaticText(
            self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.otherUser.Wrap(-1)

        self.otherUser.Hide()

        allbox.Add(
            self.otherUser, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5
        )

        self.SetSizer(allbox)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.ChatClose)
        self.Bind(wx.EVT_KEY_DOWN, self.keyDown)
        self.othernickname.Bind(wx.EVT_LEFT_DCLICK, self.otherUserInfor)
        self.inputinfors.Bind(wx.EVT_TEXT_ENTER, self.SendData)
        self.sendbtn.Bind(wx.EVT_BUTTON, self.SendData)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def ChatClose(self, event):
        event.Skip()

    def keyDown(self, event):
        event.Skip()

    def otherUserInfor(self, event):
        event.Skip()

    def SendData(self, event):
        event.Skip()


###########################################################################
## Class OtherUserInforFrame
###########################################################################


class OtherUserInforFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"云上畅谈",
            pos=wx.DefaultPosition,
            size=wx.Size(460, 300),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(460, 300), wx.DefaultSize)

        All = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(
            self, wx.ID_ANY, u"用户信息", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(
            wx.Font(
                30,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        All.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.childTouxiang = wx.StaticBitmap(
            self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(60, 60), 0
        )
        All.Add(self.childTouxiang, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        InforArea = wx.FlexGridSizer(0, 2, 0, 0)
        InforArea.SetFlexibleDirection(wx.BOTH)
        InforArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText14 = wx.StaticText(
            self, wx.ID_ANY, u"用户账号", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.m_staticText14,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childUsername = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(300, -1),
            wx.TE_READONLY,
        )
        self.childUsername.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childUsername,
            1,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT | wx.EXPAND,
            5,
        )

        self.m_staticText15 = wx.StaticText(
            self, wx.ID_ANY, u"用户昵称", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.m_staticText15,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT,
            5,
        )

        self.childNickname = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.TE_READONLY,
        )
        self.childNickname.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childNickname,
            1,
            wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT | wx.EXPAND,
            5,
        )

        self.m_staticText1511 = wx.StaticText(
            self, wx.ID_ANY, u"个性签名", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText1511.Wrap(-1)

        self.m_staticText1511.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(self.m_staticText1511, 0, wx.ALL, 5)

        self.childStyletext = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.TE_READONLY,
        )
        self.childStyletext.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                "华文新魏",
            )
        )

        InforArea.Add(
            self.childStyletext,
            1,
            wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        All.Add(InforArea, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(All)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.otherUserInforClose)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def otherUserInforClose(self, event):
        event.Skip()
