import socket
import json

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stores = []
servidores = [5001, 5002, 5003]
origin = (HOST, PORT)
tcp.bind(origin)
tcp.listen(2)
con, cliente = tcp.accept()


class store():
    def __init__(self, port, host="127.0.0.1"):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (host, port)
        self.tcp.connect(dest)

    def run(self, data):
        self.tcp.sendall(bytes(data, encoding="UTF-8"))
        message_store = self.tcp.recv(1024)
        message_store = message_store.decode("UTF-8")
        parsed_data_store = json.loads(message_store)
        print("Enviando resultados da " + parsed_data_store['store'])
        data_store = json.dumps(parsed_data_store)
        con.sendall(bytes(data_store, encoding="UTF-8"))


for servidor in servidores:
    new_store = store(servidor)
    stores.append(new_store)


while True:
    message_original = con.recv(1024)
    message = message_original.decode("UTF-8")
    parsed_data = json.loads(message)
    message_ids = {
        "product": parsed_data['product']
    }
    total_stores = {
        'total_stores': len(stores)
    }
    data = json.dumps(message_ids)
    print("Consultando estoque das lojas...")

    data_stores = json.dumps(total_stores)
    con.sendall(bytes(data_stores, encoding="UTF-8"))

    for store_item in stores:
        store_item.run(data)

    print('')

