import socket
import os

#Funktion til at haandtere requests
def handle_request(client):
    
    #1
    request = client.recv(1024).decode('utf-8')

    print("Received request:")
    print(request)
    #2
    #Find index.html filen og send den til serveren
    if "GET /index.html" in request:
        try:
            with open('index.html', 'r') as file:
                html_content = file.read()
            
            http_res = f"""HTTP/1.1 200 OK\r\n\
Content-Type: text/html; charset=UTF-8\r\n\
Connection: close\r\n\r\n\
{html_content}
"""
#Hvis filen ikke findes, så returner 404 side
        except FileNotFoundError:
            http_res = """HTTP/1.1 404 Not Found\r\n\
Content-Type: text/html; charset=UTF-8\r\n\
Connection: close\r\n\r\n\
<html>
    <head><title>404 Not Found</title></head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The requested file (index.html) was not found.</p>
    </body>
</html>
"""
# Hvis det ikke er et index.html request -> så vis 404 side
    else:
        http_res = """HTTP/1.1 404 Not Found\r\n\
Content-Type: text/html; charset=UTF-8\r\n\
Connection: close\r\n\r\n\
<html>
    <head><title>404 Not Found</title></head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The requested resource was not found.</p>
    </body>
</html>
"""
    client.sendall(http_res.encode())

    client.close()

#funktion til at starte en server
def start_server(host='127.0.0.1', port=8000):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host,port))

    print(f"Server is running on {host}:{port}")

    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        handle_request(client_socket)

if __name__ == "__main__":
    start_server()
