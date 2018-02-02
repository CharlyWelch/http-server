import sys
import socket

debug = 0 

def client (eom, message):   
    """ Client-side socket """

    s = socket.socket()
    if debug == 0: print(s)

    host = socket.gethostname()
    if debug == 0: print(host)

    try: 
        s.connect( (host, 5000) )
    except:
        print("Connection Failed")
    else:
        msg = str.encode(message)
        s.sendall(msg)

        if eom == "close":
            s.close()
            return

        elif eom == "LF":
            s.send(str.encode("\n"))
        
        raw = s.recv(len(message))
        result = raw.decode()
        s.close()

        print(result)

        if result == message:
            print("Ok: got echo")
            return True
        else:
            print("Failed: received different message: " + result)
            return False


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: client end of message")
    else:    
        client(sys.argv[1], sys.argv[2])