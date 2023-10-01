import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
"""
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    
    http://data.pr4e.org/intro-short.txt
"""
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()