# asyncio Hello World!
import asyncio

@asyncio.coroutine
def hello_world():
    while True:
        print("Hello World!")
        yield from asyncio.sleep(1.0)

# asyncio, async def / await; PEP 492 Python 3.5
async def hello_world():
    while True:
        print("Hello World!")
        await asyncio.sleep(1.0)

# asyncio, tcp сервер
async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "localhost", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.await_closed())
loop.close()

#asyncio, tpc клиент
async def tpc_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("localhost", 10001, loop=loop)

    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = "hello world"
loop.run_until_complete(tpc_echo_client(message, loop))
loop.close()
