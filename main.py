import asyncio
import web
from handle import Handle

urls = (
    '/xcx', 'Handle',
)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    app = web.application(urls, globals())
    asyncio.run(app.run())
