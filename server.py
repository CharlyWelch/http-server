import socket

debug = 0

##### Part 1: update the server so that it: 
# accumulates an incoming request into a variable
# “logs” that request by printing it to stdout
# returns a well-formed HTTP 200 response to the client.

def server():
    """ Server side socket"""
    s = socket.socket()
    if debug == 0: print(s)

    host = socket.gethostname()

    if debug == 0: print(host)

    s.bind( (host, 5000) )

    s.listen(1)

    while True:

        conn, addr = s.accept() 

        print(conn)


    message = parse_request(conn)

def parse_request(socket):
    parse_head(socket)
    parse_body(socket)
    pass

def parse_head(socket):
    #request
######### he's posting examples by 1 ########
    #while get bytes:
        #break on crlf
    #header
    #while get bytes
        #break on crlf
    #expect crlf

def parse_body(socket):
    pass
    # While get bytes:
        # break on crlf

    #expect crlf

server()