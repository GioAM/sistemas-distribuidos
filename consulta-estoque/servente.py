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


def response(stock_1, stock_2, stock_3):
    stock = {
        'loja_1':{
            'status': stock_1['status'],
            'stock': stock_1['stock']
        },
        'loja_2': {
            'status': stock_2['status'],
            'stock': stock_2['stock']
        },
        'loja_3': {
            'status': stock_3['status'],
            'stock': stock_3['stock']
        }
    }
    return stock


while True:
    message_original = con.recv(1024)
    message = message_original.decode("UTF-8")
    parsed_data = json.loads(message)


    message_ids = {
        "product": parsed_data['product']
    }
    data = json.dumps(message_ids)
    print("Consultando estoque das lojas...")
    tcp_1.sendall(bytes(data, encoding="UTF-8"))
    message_1 = tcp_1.recv(1024)
    message_1 = message_1.decode("UTF-8")
    parsed_data_1 = json.loads(message_1)

    tcp_2.sendall(bytes(data, encoding="UTF-8"))
    message_2 = tcp_2.recv(1024)
    message_2 = message_2.decode("UTF-8")
    parsed_data_2 = json.loads(message_2)

    tcp_3.sendall(bytes(data, encoding="UTF-8"))
    message_3 = tcp_3.recv(1024)
    message_3 = message_3.decode("UTF-8")
    parsed_data_3 = json.loads(message_3)
    response = response(parsed_data_1, parsed_data_2, parsed_data_3)
    print("Enviando dados do estoque")
    print(response)
    data = json.dumps(response)
    con.sendall(bytes(data, encoding="UTF-8"))
    print('')

