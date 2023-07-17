import socket

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址和端口
server_address = ('localhost', 7777)
server_socket.bind(server_address)
# 监听连接（指定最大连接数）
server_socket.listen(2)
while True:
    client_socket, client_port = server_socket.accept()
    try:
        while True:
            data = client_socket.recv(1024)
            if data:
                print("recv:", data.decode())
                client_socket.sendall(data)
            else:
                print("connection closed")
                break
    finally:
        client_socket.close()
