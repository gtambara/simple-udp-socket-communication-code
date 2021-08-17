from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('localhost', serverPort))

print("O servidor está apto a receber dados")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
 
    modifiedMessage = message.decode().upper()
 
    print(modifiedMessage + "= mensagem recebida e alterada")
 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
