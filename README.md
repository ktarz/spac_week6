# spac_week6
repository for spac week 7

# Description
This project served as an introduction to the HTTP protocol.
During the project I found that the HTTP protocol is quite unsecure at the fundamentals, when not using, what seems to be the current standard, HTTPS.

## Task 1:
The connection to the server is established with the IP-address, however most often the user will only require the domain name to connect to the server, as the domain name is translated into the IP-address by the DNS, which serves as a kind of phonebook of servers.
However, if a server host several servers, the HTTP request must include a host: header to ensure routing to the correct webpage.

## Task 2:
I found that the netcat exercise the HTTP protocols of HTTP1.1 is violated, as the request send with netcat, does not include the required headers.

## Task 3:
In the browser I found the bytesize of the index.html to be: 333 bytes
In the console I found the bytesize of the index.html to be: 322 bytes

I believe the reason the file is larger in the browser, is due to the intrepretation of the UTF-8 in the file.

## Task 4:
The task was to create a small python program that sends a HTTP request and then print this to the user.

### Getting started
#### Dependencies
- Python 3
- Libraries:
- - Socket
- index.html file
#### Executing Program
1. First you have to run the index.html through a "dummy" server created with python.
2. To do this, open the console, and run the following code in the folder of your index.html file: python -m http.server
3. Then you run the simple_http.py file in a seperate console.

## Task 5:
This task revolved around writing a program, which could answer HTTP request

### Getting started
#### Dependencies
- Python 3
- Libraries:
- - Socket
  - OS
- index.html file

#### Executing Program
1. Run the program in the console while in the correct folder.
2. Open localhost:8000/index.html in your browser.
3. Try going to another location -> try localhost:8000/bob.html
