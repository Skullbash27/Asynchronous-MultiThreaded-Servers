import socket #Activates network calling
import threading #Activates Threading
from threading import Thread # Activates to know about thread information
from database import fetch_reply #Calls fetch_reply function from the database program
from command import command_line#Calls command_line function from the command program


def server(address):
    serversock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Initates the socket connection in IPv4 and TCP
    serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #Allows the port to be reused in the operating system
    serversock.bind(address)#Binds the server to a interface(port and address) 
    print('Muti-Threaded Server!\n')
    serversock.listen(10)#Listens forconnections from the client, upto 10 can stay in the queue
    main=threading.main_thread()
    print('The Main thread is = ',main)
    print('Listening at {}'.format(address))
    return serversock

    
def accept_connection(serversock):
    while True:
        clientsock,clientaddr=serversock.accept()#Accepts the client connection
        print('Accepted connection from {}'.format(clientaddr))
        current=threading.current_thread()
        print('Active thread now is = ',current)
        communication_handler(clientsock,clientaddr)


def communication_handler(sock,address):
    try:
        while True:
            processing(sock,address)

    except EOFError:
        print('Client connection to {} has closed'.format(address))

    except Exception as other:
        print('Client on {} has error: {}'.format(address,other))

    finally:
        sock.close()

def processing(sock,address):
    client_info=keep_recv_till(sock,b'?')#Parameters passed to the keep_recv_till function to receive till it sees the '?'
    reply=fetch_reply(client_info)
    sock.sendall(reply)

def keep_recv_till(sock,suffix):
    data=sock.recv(4096)
    byte_size=len(data)
    if byte_size != 0:
        print('%d bytes processed'%byte_size)
    if not data:
        raise EOFError('Socket Closed')
    while not data.endswith(suffix):
        info=sock.recv(1024)
        if not info:
            raise IOError('Received {} then connection closed'.format(data))
        data=data+info
    return data

def start_process(client_connected,workers=5):#Specifies the number of worker threads as 5
    t=(client_connected,)#'t'stores the information of the client
    for i in range(workers):
        Thread(target=accept_connection,args=t).start() #Starts the threading process  

address=command_line('Multi-Threaded Server')
client_connected=server(address)
start_process(client_connected)








    
    


















        
    
           
