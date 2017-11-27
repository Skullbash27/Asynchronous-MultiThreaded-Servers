import socket
import time
import random
import matplotlib.pyplot as plt

client_data= {b'Best Car Maker in the World?',
              b'Best Civilian Car Maker in the World?',
              b'Biggest Planet in the Solar System?',
              b'Biggest Known Star in the Universe?',
              b'Our Galaxy?'}

bytelist=[]
timelist=[]


def client(host,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Trying to connect to Server....')
    time.sleep(7)
    start_time=float(time.time())
    try:
        sock.connect((host,port))
    except socket.timeout:
        delay = delay*2
        if delay > 20.0:
            raise RuntimeError('Server Connection failed')
            sys.exit()
    print('Server connected')
    error_happens=False
    if error_happens:
        sock.sendall(client_data[0][:-1])
        return
    sample=random.sample(list(client_data),5)#Calling the dictionary
    for info in sample:
        start_info_time=float(time.time())
        sock.sendall(info)
        bytetotal=len(info)
        print(info.decode('ascii'),keep_recv_till(sock,b'.').decode('ascii'))
        end_info_time=float(time.time())
        final_info_time=end_info_time-start_info_time
        info_in_chart=final_info_time*1000
        bytelist.append(bytetotal)
        timelist.append(info_in_chart)
    sock.close()
    end_time=float(time.time())
    final_time=end_time-start_time
    print('Time for server to process complete information is %.4f'%final_time)
    plotting()


def plotting():
    widthscale=len(timelist)/4
    figsize=(8*widthscale,6)
    fig=plt.figure(figsize=figsize)
    ax1=fig.add_subplot(1,1,1)
    plt.xlabel('TIME')
    plt.ylabel('BYTES PROCESSED')
    plt.title('Server Performance for Client 4')
    width_size=1
    bardiagram=ax1.bar(timelist,bytelist, width=width_size)
    bardiagram[0].set_color('r')
    bardiagram[1].set_color('b')
    bardiagram[2].set_color('g')
    bardiagram[3].set_color('y')
    bardiagram[4].set_color('c')
    plt.show()


def keep_recv_till(sock,suffix):
    data=sock.recv(4096)
    if not data:
        raise EOFError('Socket Closed')
    while not data.endswith(suffix):
        info=sock.recv(1024)
        if not info:
            raise IOError('Received {} then connection closed'.format(data))
        data=data+info
    return data


client('localhost',2500)
