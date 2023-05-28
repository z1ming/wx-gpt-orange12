# -*- coding: utf-8 -*-
# filename: main.py
import asyncio

import web
from handle import Handle

# 创建事件循环
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)


urls = (
    '/xcx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()