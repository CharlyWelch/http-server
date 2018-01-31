import socket

debug = 0

def server():
    s = socket.socket()
    if debug == 0: print(s)

    host = socket.gethostname()
    if debug == 0: print(host)

    #client side terminology is connect, server side is bind
    s.bind( (host, 12345) )

    s.listen(5)

    #loop forever listening for client connections.
    while True:
        #block (wait) for a client connection
        conn, addr = s.accept() #established connection with client
        message = ""
        while True:
            part = conn.recv(16)
            if len(part) == 0:
                break
            else:
                message += part
        message = conn.recv(16)
        if debug == 1: print(message)

        if message.decode() == "q":
            break
        conn.close()

server()