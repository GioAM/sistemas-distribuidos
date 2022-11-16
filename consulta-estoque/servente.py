import socket
import json
from threading import Thread

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidores = [5001, 5002, 5003]
stores = []
origin = (HOST, PORT)

tcp.bind(origin)
tcp.listen(2)


class store():
    def __init__(self, port, host='127.0.0.1'):
        Thread.__init__(self)
        self.port = port
        self.host = host
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, self.port)
        self.tcp.connect(dest)

    def run(self, data):
        self.tcp.sendall(bytes(data, encoding="UTF-8"))
        message_com = self.tcp.recv(1024)
        message_com = message_com.decode("UTF-8")
        con.sendall(bytes(message_com, encoding="UTF-8"))
        parsed_data_com = json.loads(message_com)
        print(parsed_data_com)


con, cliente = tcp.accept()

for servidor in servidores:
    store_server = store(servidor)
    stores.append(store_server)

while True:
    message_original = con.recv(1024)
    message = message_original.decode("UTF-8")
    parsed_data = json.loads(message)
    stores_total = {
        "stores": len(servidores)
    }
    stores_total_json = json.dumps(stores_total)
    con.sendall(bytes(stores_total_json, encoding="UTF-8"))
    print("Recebendo requisição de cotação")
    message_ids = {
        "product": parsed_data['product']
    }
    print(message_ids)
    data = json.dumps(message_ids)
    print("Resultados:")
    for store_item in stores:
        store_item.run(data)
    stores = []

