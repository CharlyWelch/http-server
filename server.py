import socket

debug = 0

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

        message = b''
        
        while True:
            data = conn.recv(1)

            if data == b'':
                break

            if data == b'\n':
                break
            
            message += data
            
        conn.send(message)

        conn.close()

        if message.decode() == "q":
            break

server()