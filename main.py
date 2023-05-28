# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from shared_queue import global_queue
import shared_queue
import threading


# 消费者线程，从队列中获取元素进行消费
def consumer():
    while True:
        if not global_queue.empty():
            replyMsg = global_queue.get()
            print("消费元素:", replyMsg)
            replyMsg.send()

        else:
            # 队列为空，进行其他操作或休眠一段时间
            print("队列为空，进行其他操作或休眠...")
            # 在这里添加需要执行的操作或休眠的逻辑
            # ...

urls = (
    '/xcx', 'Handle',
)

if __name__ == '__main__':
    # 创建并启动消费者线程
    consumer_thread = threading.Thread(target=consumer)
    # 启动消费者线程
    consumer_thread.start()
    # 启动生产者线程（假设您已经有了这个线程）
    app = web.application(urls, globals())
    app.run()
    # 等待消费者线程结束
    consumer_thread.join()