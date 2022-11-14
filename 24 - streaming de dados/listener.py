import socket
import time

HOST = 'localhost'
PORT = 3000


#Criando Socket
s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta {PORT}')

#Criando o listen
s.listen(5)

#Criando a variavel para aceitar, retiorna uma tupla
#conn : file descriptor - conexão
conn, adress = s.accept()
print(f'Recebendo solicitação de {adress}')

#Criando lista de mensagens de comunicações
messages = [
   'Mensagem A',
     'Mensagem B',
     'Mensagem C',
     'Mensagem D',
     'Mensagem E',
     'Mensagem F',
     'Estou animado com o curso'
     ]

## Iterando as mensagens
for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close()