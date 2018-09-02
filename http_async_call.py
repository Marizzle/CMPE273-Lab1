import asyncio
import requests

web_hook_url = 'https://webhook.site/00ad0d5b-4adb-4206-b94c-94e1e14ef5db'

@asyncio.coroutine
def main():
    loop = asyncio.get_event_loop()

    f1 = loop.run_in_executor(None, requests.get, web_hook_url)
    f2 = loop.run_in_executor(None, requests.get, web_hook_url)
    f3 = loop.run_in_executor(None, requests.get, web_hook_url)

    r1 = yield from f1
    r2 = yield from f2
    r3 = yield from f3

    print(r1.headers['Date'])
    print(r2.headers['Date'])
    print(r3.headers['Date'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
