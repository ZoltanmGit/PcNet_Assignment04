import sys
import socket
import hashlib

def file_as_bytes(file):
    with file:
        return file.read()

argServerIp = sys.argv[1]
argServerPort = sys.argv[2]
argCheckServerIp = sys.argv[3]
argCheckServerPort = sys.argv[4]
argFileID = sys.argv[5]
argFilePath = sys.argv[6]

#UPLOADING THE CHECKSUM
check_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
check_sock.connect((argCheckServerIp,int(argCheckServerPort)))
#Calculate Chekcsum
checkSum = hashlib.md5(file_as_bytes(open(argFilePath, 'rb'))).hexdigest()
stringForCheck = "BE|"+argFileID+"|"+str(60)+"|"+str(sys.getsizeof(checkSum))+"|"+checkSum
check_sock.send(stringForCheck.encode())
Reply = check_sock.recv(1024).decode()
#print("Got: "+Reply)
check_sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#print("Attempt to reconnect")
sock.connect((argServerIp,int(argServerPort)))
sendFile = open(argFilePath, 'rb')
sendbyte = sendFile.read(1024)
while (sendbyte):
    #print("Sending..")
    sock.send(sendbyte)
    sendbyte = sendFile.read(1024)
sock.shutdown(socket.SHUT_WR)
sendFile.close()

#print("Sent!")    