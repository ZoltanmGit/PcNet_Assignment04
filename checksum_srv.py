import sys

argumentIP = sys.argv[1]
argumentPort = sys.argv[2]

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((argumentIP,int(argumentPort)))
serv_sock.listen(1)