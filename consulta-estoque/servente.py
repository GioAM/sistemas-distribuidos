import socket
import json

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origin = (HOST, PORT)

tcp.bind(origin)
tcp.listen(2)

dest = (HOST, 5001)
tcp_1.connect(dest)

dest = (HOST, 5002)
tcp_2.connect(dest)

dest = (HOST, 5003)
tcp_3.connect(dest)
con, cliente = tcp.accept()

while True:
    message_original = con.recv(1024)
    message = message_original.decode("UTF-8")
    parsed_data = json.loads(message)
    print(message)

    message_ids = {
        "product": parsed_data['product']
    }
    data = json.dumps(message_ids)
    tcp_1.sendall(bytes(data, encoding="UTF-8"))
    message_1 = tcp_1.recv(1024)
    message_1 = message_1.decode("UTF-8")
    parsed_data_1 = json.loads(message_1)
    print(parsed_data_1)

    tcp_2.sendall(bytes(data, encoding="UTF-8"))
    message_2 = tcp_2.recv(1024)
    message_2 = message_2.decode("UTF-8")
    parsed_data_2 = json.loads(message_2)

    tcp_3.sendall(bytes(data, encoding="UTF-8"))
    message_3 = tcp_3.recv(1024)
    message_3 = message_3.decode("UTF-8")
    parsed_data_3 = json.loads(message_3)


    print(parsed_data_2)
    print(parsed_data_3)
