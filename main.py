# -*- coding: utf-8 -*-
# filename: main.py
import asyncio
import web
from handle import Handle

urls = (
    '/xcx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    app.run()

