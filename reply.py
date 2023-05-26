# -*- coding: utf-8 -*-
# filename: reply.py
import json
import time
import post

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        super().__init__()
        self.__dict__ = dict()
        self.__dict__['ToUserName'] = toUserName
        self.__dict__['FromUserName'] = fromUserName
        self.__dict__['CreateTime'] = int(time.time())
        self.__dict__['Content'] = content

    def send(self):
        # 发送gpt
        reply = post.postGpt(self.__dict__['Content'])

        # 将gpt的回答返回给用户
        post.postXcxTxt(self.__dict__['ToUserName'], reply)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict__ = dict()
        self.__dict__['ToUserName'] = toUserName
        self.__dict__['FromUserName'] = fromUserName
        self.__dict__['CreateTime'] = int(time.time())
        self.__dict__['MediaId'] = mediaId

    def send(self):
        print(json.dumps(**self.__dict__))