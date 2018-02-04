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


        strMessage = message.decode()

        print(message)

        if strMessage == "testOK":
            ok = response_ok()
            conn.send(ok.encode())

        if strMessage == "testError":
            error = response_error()
            conn.send(error.encode())

        conn.close()

        if message.decode() == 'q':
            break

def response_ok():
    """ Return an OK response - for use if message is properly received """
    return "HTTP/1.1 200: OK"

def response_error():
    """ Return an error response if message not properly received """
    return "HTTP/1.1 500: Internal Server Error"

    
server()