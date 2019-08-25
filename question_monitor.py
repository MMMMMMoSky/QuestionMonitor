#!/usr/bin/env python3
# coding: utf-8

from wxpy import Bot
from email_sender import sendTextEmail


class QuestionMonitor:
    '''[实现了对微信群聊消息的过滤监听, 将获取到的消息发送邮件]

    需要在 _capturedContent() 函数中设置邮件地址

    Attributes:
        _groups: 群聊名称列表, 接收到的消息的群聊名称需要包含 groups 的至少一个字符串
        _contents: 消息内容, 接收到的消息内容需要包含 contents 中的至少一个字符串
        _bot: wxpy.Bot 类的实例
    '''

    def __init__(self, groups: list = None, contents: list = None):
        self._groups = groups
        self._contents = contents
        self._bot = None

    # just for debug
    # def getBot(self):
    #     return self._bot

    def setGroups(self, groups: list = None):
        if groups != None:
            self._groups = groups

    def setContents(self, contents: list = None):
        if contents != None:
            self._contents = contents

    def startMonitor(self):
        '''[对 groups 群聊开始监听, 检查是否出现了包含 contents 内容的消息]

        登陆微信, 注册消息接受函数, 接收到的消息将传递给 _checkMessage() 进行过滤
        不满足条件的消息将会被过滤, 满足条件的消息将会传递给 _capturedContent() 进行下一步处理
        '''

        if self._groups == None or len(self._groups) == 0:
            print('Error: starting monitor with an empty [groups] list')
            print('       please set [groups] with setGroups() method or')
            print('       ! you will get no message !')

        if self._contents == None or len(self._contents) == 0:
            print('Error: starting monitor with an empty [contents] list')
            print('       please set [contents] with setContents() method or')
            print('       ! you will get no message !')

        self._bot = Bot()
        @self._bot.register()
        def _receiveMessage(msg):
            self._checkMessage(msg)

    def _capturedContent(self, msg):
        sender = '[Sender Email Address]'
        receivers = ['[Receiver List]']
        host = '[Email Host Address]'
        user = sender
        password = '[Your Password]'
        subject = 'WeChat Unread Message'
        text = str(msg)

        result = sendTextEmail(sender, receivers,
                               (host, user, password),
                               subject, text)

        print('Sending...', END = '')
        print(str(msg))
        print('Ok!' if result else 'Failed')
        print('- ' * ((len(str(msg)) // 2) + 1))

    def _checkMessage(self, msg):
        if msg.member == None:  # 非群聊消息
            return

        flag = False
        for group in self._groups:
            if group in msg.chat.name:
                flag = True
                break
        if flag == False:
            return

        flag = False
        for content in self._contents:
            if content in msg.text:
                flag = True
                break

        if flag == True:
            self._capturedContent(msg)
