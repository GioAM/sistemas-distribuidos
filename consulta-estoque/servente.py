import socket

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origin = (HOST, PORT)
tcp.bind(origin)
tcp.listen(2)

while True:
    con, cliente = tcp.accept()

con.close()