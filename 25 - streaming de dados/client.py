import socket
import time

HOST = 'localhost'
PORT =  3000

#Realizando a conexão
s = socket.socket()
s.connect((HOST, PORT))

#Criando um laço de repetição para iterar quando a variável data for true
#1024: Quanditdados de bytes recebidos pelo listener
#UTF-8 facilitando a renderização da mensagem
while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)