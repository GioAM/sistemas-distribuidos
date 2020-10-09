import socket
import time
import sys

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.249.1'
port = 5555
destino = (host, port)
tcp.connect(destino)
while True:
    time.sleep(1)
    tcp.send(str.encode("Are you Alive?"))
    inicio = time.time()
    mensagem = tcp.recv(1024)
    mensagem = mensagem.decode("UTF-8")

    if int(time.time() - inicio) >= 5:
        print("Processo com erro")
        sys.exit()
    print(mensagem)