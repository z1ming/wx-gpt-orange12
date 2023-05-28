import asyncio
import web
from handle import Handle

urls = (
    '/xcx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    loop = asyncio.get_event_loop()
    loop.create_task(app.run())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
