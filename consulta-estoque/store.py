import socket
import json


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