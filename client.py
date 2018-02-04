import sys
import socket

def make_request(message):
    """ Build packet for http request """
    host = socket.gethostname()
    REQUEST = "GET"
    VERSION = "HTTP/1.1"
    CRLF = "\r\n"

    request = REQUEST + " " + VERSION + CRLF

    headers = "Host: {0}".format(host) + CRLF

    head = request + headers
    body = message + CRLF
    return head + CRLF + body + CRLF


def client(eom, message):   
    """ Client-side socket """

    s = socket.socket()

    host = socket.gethostname()

    try: 
        s.connect( (host, 5000) )
    except:
        print("Connection Failed")
    else:
        packet = make_request(message)
        s.sendall(packet.encode())

        if eom == "close":
            s.close()
            return

        elif eom == "LF":
            s.send(str.encode("\n"))

        result = parse_response( s )  #I'm a bit lost between this and lines 46-54 

        buffer_length = 8
        message_complete = False
        response = ''
        
        while not message_complete:
            part = s.recv(buffer_length)
            response += part.decode('utf8')
            if len(part)< buffer_length:
                break
        
        response_error(response, message)
    
        s.close()

        print(message)
        return(message)


def parse_response(message):
    """ parse the http response """
    result = message.decode()
    return result
    
def response_error(response, message):
    """ return a 500: Internal server error message """
    if response != message:
        return "500: Internal server error"

if __name__ == "__main__": 
    
    client(sys.argv[1], sys.argv[2])