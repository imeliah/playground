import socket

# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
server_address = ('localhost', 7777)
client_socket.connect(server_address)
try:
    message = "hello"
    client_socket.sendall(message.encode())
    resp = client_socket.recv(1024)
    print("recv:", resp.decode())
finally:
    client_socket.close()
