import sys
import socket
import select
import string

argumentIP = sys.argv[1]
argumentPort = sys.argv[2]

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((argumentIP,int(argumentPort)))
serv_sock.listen(10)

inputs = [serv_sock]
clients = []
CheckSumList = []
#print("CheckServer Running...")
while True:
    readable, _ , _ = select.select(inputs,[],[])
    for s in readable:
        if s is serv_sock:
            new_cient, cli_addr = s.accept()
            inputs.append(new_cient)
            clients.append(new_cient)
            #print("CLient connected")
        else:
            ReceivedString = s.recv(1024)
            ReceivedString = ReceivedString.decode()
            ReceivedString = ReceivedString.split('|')
            if(ReceivedString[0] == "BE"):
                s.send("OK".encode())
                #print("Received __BE__ sent __OK__")
                CheckSumList.append((ReceivedString[1],ReceivedString[3],ReceivedString[4]))
            elif(ReceivedString[0] == "KI"):
                bIsFound = False
                SelectedData = None
                for i in CheckSumList:
                    if(i[0] == ReceivedString[1]):
                        bIsFound = True
                        SelectedData = i
                        CheckSumList.remove(i)
                        break
                if(bIsFound):
                    ReplyString = SelectedData[0]+"|"+SelectedData[2]
                    s.send(ReplyString.encode())
                    #print("Received __KI__ sent __"+ReplyString+"__")
                else:
                    
                    s.send("0|".encode())
                    #print("Received __KI__ sent __0|__")
            inputs.remove(s)
            clients.remove(s)
serv_sock.close()