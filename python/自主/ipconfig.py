import socket

while True:
    ips = input('请输入网址：')
    result = socket.getaddrinfo(ips, None)
    print(ips, '的ip是:', result[0][4][0])
