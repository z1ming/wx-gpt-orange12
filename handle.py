# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive_json
import post
import json


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

    # def POST(self):
    #     try:
    #         webData = web.data()
    #         print("Handle Post webdata is ", webData)
    #         # 后台打日志
    #         recMsg = receive.parse_xml(webData)
    #         if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
    #             toUser = recMsg.FromUserName
    #             fromUser = recMsg.ToUserName
    #             content = str(post.postGpt(recMsg.Content))
    #             replyMsg = reply.TextMsg(toUser, fromUser, content)
    #             return replyMsg.send()
    #         else:
    #             print("暂且不处理")
    #             return "success"
    #     except Exception as e:
    #         return str(e)
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            recMsg = receive_json.parse_json(webData)
            print('recMsg: ', recMsg)
            if isinstance(recMsg, receive_json.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content
                print('toUser: ', toUser, 'fromUser: ', fromUser, 'content: ', content)
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                print('replyMsg: ', replyMsg)
                return replyMsg.send()
            # 后台打日志
            return "success"
        except Exception as e:
            return str(e)
