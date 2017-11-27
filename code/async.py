import asyncio#Activates asynchronous programming
from database import fetch_reply
from command import command_line


def process(reader,writer):
    address=writer.get_extra_info('peername')#Stores the client information inside address
    print('Accepted connection from {}'.format(address))
    while True:
        info=b''
        while not info.endswith(b'?'):
            more_info=yield from reader.read(4096)#continously receives information from the client
            if not more_info:
                if info:
                    print('Client {} data not framed'.format(address))
                else:
                    print('Client {} socket closed'.format(address))
                return
            info=more_info+info
            answer=fetch_reply(info)
            writer.write(answer)


address=command_line('Asyncio Server')
loop=asyncio.get_event_loop()#calls the event loop
coro=asyncio.start_server(process,*address)#starts the server
server=loop.run_until_complete(coro)#Make the code run untill all client information is processed
print('Asynchronous Server!\n')
print('Listening at {}'.format(address))

try:
    loop.run_forever()#Continously keeps the server running and listening for client conenctions

finally:
    server.close()
    







    
