from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

dados = input('Coloque sua frase em letras minúsculas:')
cor = input('Coloque a sua cor favorita:[1-azul,2-vermelho,3-verde,4-amarelo,5-branco]')

switchCase = {
        1: '\033[34m',
        2: '\033[31m',
        3: '\033[32m',
        4: '\033[33m',
        5: '\033[37m'
    }

print(switchCase[int(cor)])

# mensagem = switchCase[int(cor)] + " " + dados + " " + '\033[37m'
mensagem = dados

# Envio da imagem em bytes pro servidor
clientSocket.sendto(mensagem.encode(),(serverName, serverPort))

# Recebimento da mensagem modificada do servidor
mensagemNova, serverAddress = clientSocket.recvfrom(2048)

# Mostra a mensagem modificada como string
print(mensagemNova.decode())

# Fecha o socket/conexão com o servidor
clientSocket.close()


