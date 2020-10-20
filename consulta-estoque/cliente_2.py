import socket
import json

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta


def showResult(stock_data):
    print(stock_data['store'])
    if stock_data['status'] == 'not_exist':
        print('  Produto não encontrado')
    elif stock_data['status'] == 'not_available':
        print('  Produto sem estoque')
    else:
        print('  Estoque: ' + stock_data['stock'])


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

while True:
    product_id = input()
    stock_total = 0
    message = {
        'product': product_id
    }
    data = json.dumps(message)
    print("Consultando estoque das lojas...")
    tcp.sendall(bytes(data, encoding="UTF-8"))
    message = tcp.recv(1024)
    message = message.decode("UTF-8")
    parsed_data = json.loads(message)
    for i in range(int(parsed_data['total_stores'])):
        message = tcp.recv(1024)
        message = message.decode("UTF-8")
        stock_data = json.loads(message)
        showResult(stock_data)
        stock_total = stock_total + int(stock_data['stock'])
    print('---> ESTOQUE TOTAL: ' + str(stock_total) + " <---")