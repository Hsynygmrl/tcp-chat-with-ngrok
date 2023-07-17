import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
# print(local_ip)
host = 'localhost' # bağlı olduğun netin ip al
port = 9999
address = (host, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)
print ("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)
while True:
    output = conn.recv(2048) # karşıdan veri alma işlemi
    print ('Abdullah:',output.decode()) # karşıdan alınan veriyi decode et ve yaz
    conn.send(str.encode(str(input('Hüseyin:')))) # karşıya ack' i encode et ve yolla
server_socket.close()
