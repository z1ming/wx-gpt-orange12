# -*- encoding: utf-8 -*-
"""
@File: timer.py    
@Author: mengziming021
@Time: 2023/5/23 8:19 下午 
"""
import threading

def callback():
    print("success")



if __name__ == '__main__':
    # 启动定时器，在 5 秒后执行回调函数
    timer = threading.Timer(5, callback)
    timer.start()