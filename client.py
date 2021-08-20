from socket import *
import tkinter as tk

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

def botaoPressionado(event):
    dados = entry.get()
    mensagem = dados
    
    # Envio da mensagem em bytes pro servidor
    clientSocket.sendto(mensagem.encode(),(serverName, serverPort))

    # Recebimento da mensagem modificada do servidor
    mensagemNova, serverAddress = clientSocket.recvfrom(2048)

    # Mostra a mensagem modificada como string
    try:
        resposta.tk.destroy()
    except (NameError, AttributeError):
        pass
    resposta.config(text="Retorno do servidor:\n" + mensagemNova.decode(), bg="green")
    resposta.pack()

window = tk.Tk()
window.geometry("300x220")
label = tk.Label(text="Frase mandada ao servidor:")
entry = tk.Entry()

respostaFrame = tk.Frame(window, height = "80", width = "110", bg = "green")
respostaFrame.pack(fill = 'both')
resposta = tk.Label(respostaFrame, text="", fg="white", bg="green", height = "5", wraplength = 160)
resposta.pack()

b1 = tk.Button(window, text="click", bg="red", fg="white")

entry.pack()
b1.pack()
label.pack()

b1.bind('<Button>', botaoPressionado)

window.mainloop()

# Fecha o socket/conexão com o servidor
clientSocket.close()

