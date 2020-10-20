import socket
import json
from store import store

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stores = []
servidores = [5001, 5002, 5003]
origin = (HOST, PORT)
tcp.bind(origin)
tcp.listen(2)
con, cliente = tcp.accept()


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

