# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive_json
import asyncio
from shared_queue import global_queue

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "mengziming021"  # 请按照公众平台官网\基本配置中信息填写

            data_list = [token, timestamp, nonce]
            data_list.sort()
            sha1 = hashlib.sha1()
            for item in data_list:
                sha1.update(item.encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return str(e)

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            recMsg = receive_json.parse_json(webData)
            if isinstance(recMsg, receive_json.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                print('replyMsg: ', replyMsg.__dict__)
                # replyMsg.send()
                global_queue.put(replyMsg)
            return 'success'  # 立即返回'success'
        except Exception as e:
            print(str(e))