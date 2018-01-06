import socket
import time
import random #Activates random data calling from dataset
import matplotlib.pyplot as plt #acivates data visualization with matplotlib

client_data= {b'Best team in Cricket?',
              b'Best team in IPL?',
              b'Flow of electrons?',
              b'Fastest Train in the World?',
              b'Best Band in the World?'}#Dataset from which client will select and send information to the server

bytelist=[]
timelist=[]


def client(host,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Trying to connect to Server....')
    time.sleep(10)
    start_time=float(time.time())
    try:
        sock.connect((host,port)) # Connects to the server address and port
    except socket.timeout: #Timeout set to keep teying again until a specific condition
        delay = delay*2
        if delay > 20.0:
            raise RuntimeError('Server Connection failed')
            sys.exit()  
    print('Server connected')
    error_happens=False
    if error_happens:
        sock.sendall(client_data[0][:-1])
        return
    sample=random.sample(list(client_data),5)#Calling the dataset to pick data randomly, number 5 put because dataset contains 5 feilds of information
    for info in sample:
        start_info_time=float(time.time())
        sock.sendall(info)
        bytetotal=len(info)
        print(info.decode('ascii'),keep_recv_till(sock,b'.').decode('ascii'))#data from the client is decoded to the ascii format
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
    widthscale=len(timelist)/4#widthsize of the bar chart is initialized
    figsize=(10*widthscale,6)
    fig=plt.figure(figsize=figsize)
    ax1=fig.add_subplot(1,1,1)
    plt.xlabel('TIME')
    plt.ylabel('BYTES PROCESSED')
    plt.title('Server Performance for Client 1')
    width_size=1
    bardiagram=ax1.bar(timelist,bytelist, width=width_size)#the bar chart is called and plotted here
    bardiagram[0].set_color('r')
    bardiagram[1].set_color('b')
    bardiagram[2].set_color('g')
    bardiagram[3].set_color('y')
    bardiagram[4].set_color('c')
    plt.show()#displays the information


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


client('192.168.56.1',2500)
