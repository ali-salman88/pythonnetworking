import socket

so= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
so.bind(('127.0.0.1', 3000))
print('Listening to {}'.format(so.getsockname()))
data, address= so.recvfrom(1024)
text=data.decode ('ascii')
print('client at {} date :{}'.format (address, text))
text='the client data was {} bytes long'.format(len(data))
data=text.encode('ascii')
so.sendto(data,address)