import socket, time
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('ngrok ip address of server side',ngrok port))
while True:
    data = str.encode(input('Abdullah:'))
    client_socket.send(data)
    # while client_socket.recv(2048) != str(500):
    print('Hüseyin:',client_socket.recv(2048).decode()) # karşıdan alınan
client_socket.close()

