# -*- coding: utf-8 -*-
# filename: reply.py
import json
import time

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict__ = dict()
        self.__dict__['ToUserName'] = toUserName
        self.__dict__['FromUserName'] = fromUserName
        self.__dict__['CreateTime'] = int(time.time())
        self.__dict__['Content'] = content

    # def send(self):
    #     XmlForm = """
    #         <xml>
    #             <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
    #             <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
    #             <CreateTime>{CreateTime}</CreateTime>
    #             <MsgType><![CDATA[text]]></MsgType>
    #             <Content><![CDATA[{Content}]]></Content>
    #         </xml>
    #         """
    #     return XmlForm.format(**self.__dict__)

    def send(self):
        print(self.__dict__)

class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict__ = dict()
        self.__dict__['ToUserName'] = toUserName
        self.__dict__['FromUserName'] = fromUserName
        self.__dict__['CreateTime'] = int(time.time())
        self.__dict__['MediaId'] = mediaId

    # def send(self):
    #     XmlForm = """
    #         <xml>
    #             <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
    #             <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
    #             <CreateTime>{CreateTime}</CreateTime>
    #             <MsgType><![CDATA[image]]></MsgType>
    #             <Image>
    #             <MediaId><![CDATA[{MediaId}]]></MediaId>
    #             </Image>
    #         </xml>
    #         """
    #     return XmlForm.format(**self.__dict__)

    def send(self):
        print(json.dumps(**self.__dict__))