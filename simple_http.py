import socket

#Opretter socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Forbinder socket til localhost
try:
    sock.connect(('127.0.0.1', 8000))
#Error handling - luk forbindelse ved fejl og print fejlbesked
except socket.error as err:
    print(f"Socket error: {err}")
    sock.close()
    exit(1)

#Lav request og send det
request = "GET / HTTP/1.1\r\n"
request +="Host: www.index.com\r\n"
request +="Connection: close\r\n\r\n"
try:
    sock.sendall(request.encode())
#Error handling - luk forbindelse ved fejl og print fejlbesked
except socket.error as err:
    print(f"Socket error: {err}")
    sock.close()
    exit(1)

#Fang http response og print det
try:
    response = sock.recv(4096)
    print(response.decode())
#Error handling - luk forbindelse ved fejl og print fejlbesked
except socket.error as err:
    print(f"Socket error: {err}")
    sock.close()
    exit(1)

sock.close()
