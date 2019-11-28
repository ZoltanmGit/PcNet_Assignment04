import sys
import socket

argServerIp = sys.argv[1]
argServerPort = sys.argv[2]
argCheckServerIp = sys.argv[3]
argCheckServerPort = sys.argv[4]
argFileName = sys.argv[5]
argFilePath = sys.argv[6]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((argServerIp,int(argServerPort)))
