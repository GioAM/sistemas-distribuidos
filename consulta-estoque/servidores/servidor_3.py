import socket
import json
import csv

HOST = ''  # Endereco IP do Servidor
PORT = 5003  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origin = (HOST, PORT)
tcp.bind(origin)
tcp.listen(2)
con, cliente = tcp.accept()


def get_stock():
    stock = {}
    with open('../estoque/estoque_3.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock[row['product_id']] = row['stock']
    return stock


def response(product_id):
    print("Consultando estoque...")
    stock = get_stock()
    if product_id in stock.keys():
        if int(stock[product_id]) > 0:
            status = "available"
            stock = stock[product_id]
        else:
            status = "not_available"
            stock = 0
    else:
        status = "not_exist"
        stock = 0
    info = {
        'status': status,
        'stock': stock
    }
    return info


while True:
    message = con.recv(1024)
    message = message.decode("UTF-8")
    parsed_data = json.loads(message)
    product_id = parsed_data['product']
    print("Recebendo requisição para o produto " + product_id)
    data = json.dumps(response(product_id))
    con.sendall(bytes(data, encoding="UTF-8"))
    print("Enviando cotação para o produto " + product_id)

