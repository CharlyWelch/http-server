"""Client"""
import sys
import socket

debug = True

def client (message):
    s = socket.socket()
    if debug == 0: print(s)
    host = socket.gethostname()
    if debug == 0: print(host)

    try: 
        s.connect( (host, 12345))
    except:
        print("Connection Failed")
    else:

        s.send(str.encode(message))

        raw = s.recv(len(message))
        result = raw.decode()

        s.close()

        if result == message:
            print("Ok: got echo")
            return True
        else:
            print("Failed: received different message: " + result)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: client message")
    else:    
        client(sys.argv[1])