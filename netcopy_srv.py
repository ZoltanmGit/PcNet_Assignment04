import sys

argServerIp = sys.argv[1]
argServerPort = sys.argv[2]
argCheckServerIp = sys.argv[3]
argCheckServerPort = sys.argv[4]
argFileName = sys.argv[5]
argFilePath = sys.argv[6]

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((argServerIp,int(argServerPort)))
serv_sock.listen(1)