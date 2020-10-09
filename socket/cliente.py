import socket, pickle
import time, random

HOST = ''
PORT = 5555
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)
tcp.bind(origem)
tcp.listen(2)
con, cliente = tcp.accept()

while True:
    mensagem = con.recv(1024)
    mensagem = mensagem.decode("UTF-8")
    print(mensagem)
    time.sleep(random.randint(0, 5))
    con.send(str.encode("I am Alive!"))