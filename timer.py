# -*- encoding: utf-8 -*-
"""
@File: timer.py    
@Author: mengziming021
@Time: 2023/5/23 8:19 下午 
"""
import threading
import requests

# 全局变量，用于保存接口返回值
access_token = None


def fetch_data():
    global access_token

    # 发起请求
    response = requests.get(
        'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxd26ba0053c3ce36a&secret=fbebb6c054183db0f4b8ef6bb5ae2640')
    print('获取 access_token 结果：', response)
    # 检查响应状态码
    if response.status_code == 200:
        # 请求成功
        data = response.json()  # 获取响应数据（假设是 JSON 格式）

        # 将数据保存在全局变量中
        access_token = data['access_token']

        # 设置下一次请求的定时器（1.5 小时后）
        timer = threading.Timer(1.5 * 60 * 60, fetch_data)
        timer.start()
    else:
        # 请求失败
        print('请求失败:', response.status_code)
        # 设置下一次请求的定时器（1.5 小时后）
        timer = threading.Timer(1.5 * 60 * 60, fetch_data)
        timer.start()


# 启动定时器
fetch_data()
