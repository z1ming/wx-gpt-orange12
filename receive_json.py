# -*- encoding: utf-8 -*-

import json

"""
@File: receive_json.py.py    
@Author: mengziming021
@Time: 2023/5/25 8:05 下午 
"""
def parse_json(web_data):
    if len(web_data) == 0:
        return None
    jsonData = json.loads(web_data)
    msg_type = jsonData["MsgType"]
    if msg_type == 'text':
        return TextMsg(jsonData)
    elif msg_type == 'image':
        return ImageMsg(jsonData)

class Msg(object):
    def __init__(self, jsonData):
        self.ToUserName = jsonData["ToUserName"]
        self.FromUserName = jsonData["FromUserName"]
        self.CreateTime = jsonData["CreateTime"]
        self.MsgType = jsonData["MsgType"]
        self.MsgId = jsonData["MsgId"]


class TextMsg(Msg):
    def __init__(self, jsonData):
        super().__init__(jsonData)
        self.Content = jsonData["Content"]


class ImageMsg(Msg):
    def __init__(self, jsonData):
        super().__init__(jsonData)
        self.PicUrl = jsonData["PicUrl"]
        self.MediaId = jsonData["MediaId"]
