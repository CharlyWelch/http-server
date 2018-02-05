import socket

debug = False

def server():
    """ Server side socket"""
    s = socket.socket()
    if debug: print(s)

    host = socket.gethostname()
    if debug: print(host)
    
    address = (host, 5000)

    s.bind( address )

    s.listen(1)

    while True:

        conn, addr = s.accept() 

        if debug: print(conn)
        
        message = b''

        while True:
            data = conn.recv(1)

            if data == b'':
                break
            if data == b'\n':
                break

            message += data

        parse_request(message)

        print(message)

        # if strMessage == "testOK":
        #     ok = response_ok()
        #     conn.send(ok.encode())

        # if strMessage == "testError":
        #     error = response_error()
        #     conn.send(error.encode())

        conn.close()

        if message.decode() == 'q':
            break

def response_ok():
    """ Return an OK response - for use if message is properly received """
    return "HTTP/1.1 200: OK"

def response_error():
    """ Return an error response if message not properly received """
    return "HTTP/1.1 500: Internal Server Error"

def parse_request(message):
    str = message.decode()
    req_parts = str.split('\r\n')
    req = req_parts[0].split(' ')
    host = req_parts[1].split(' ')
    resource = req[1]

    response = resource

    if req[0] != "GET":
        response = "Accepting only GET requests"
    
    if req[2] != "HTTP/1.1":
        response = "Incorrect HTTP version. Use HTTP\1.1"

    if host[0] != "Host:":
        response = "Proper host header not included"

    else:
        response = "URI: {0}".format(resource)

    return response
    

# The function should only accept GET requests. Any other request method should raise an appropriate Python exception.
# The function should only accept HTTP/1.1 requests. A request of any other HTTP version should raise an appropriate Python exception.
# The function should validate that a proper Host header was included in the request and if not, raise an appropriate Python exception.
# The function should validate that the request is well-formed. If the request is malformed in some way, it should raise an appropriate Python exception.
# If none of the conditions above arise, the function should return the URI from the request.

    
server()