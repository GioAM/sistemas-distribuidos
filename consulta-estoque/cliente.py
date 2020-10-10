import socket
import json

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
while True:
    product_id = input()
    message = {
        'product': product_id
    }
    data = json.dumps(message)
    tcp.sendall(bytes(data, encoding="UTF-8"))
