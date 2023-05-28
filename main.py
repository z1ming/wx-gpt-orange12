import asyncio
import web
from handle import Handle

urls = (
    '/xcx', 'Handle',
)

async def run_app():
    app = web.application(urls, globals())
    await app.run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_app())
