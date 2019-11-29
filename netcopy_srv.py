import sys
import socket
import hashlib

def file_as_bytes(file):
    with file:
        return file.read()
#Command Line arguments
argServerIp = sys.argv[1]
argServerPort = sys.argv[2]
argCheckServerIp = sys.argv[3]
argCheckServerPort = sys.argv[4]
argFileID = sys.argv[5]
argFilePath = sys.argv[6]
#Create, Bind and listen for client
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((argServerIp,int(argServerPort)))
serv_sock.listen(1)

#print('NetCopy Server Running...')
while True:
    client = serv_sock.accept()
    #print("Client connected.")
    receivedFile = open(argFilePath, 'wb')
    data = client[0].recv(1024)
    while (data):
        #print("Writing...")
        receivedFile.write(data)
        data = client[0].recv(1024)
    receivedFile.close()
    #print("Received!")
    client[0].close()

    checkSum = hashlib.md5(file_as_bytes(open(argFilePath, 'rb'))).hexdigest()
    QueryString = "KI|"+argFileID
    check_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    check_sock.connect((argCheckServerIp,int(argCheckServerPort)))
    check_sock.send(QueryString.encode())
    Reply = check_sock.recv(1024)
    if(checkSum == Reply.decode()[len(argFileID)+1:] and argFileID == Reply.decode()[:len(argFileID)]):
        print("CSUM OK")
    else:
        print("CSUM CORRUPTED")

    exit()