import socket
import json

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta


def showResult(stock, product_id):
    print("-> Estoque para o produto " + product_id)
    loja_1 = stock['loja_1']
    loja_2 = stock['loja_2']
    loja_3 = stock['loja_3']
    stock_total = int(loja_1['stock']) + int(loja_2['stock']) + int(loja_3['stock'])
    print('Loja 1')
    if loja_1['status'] == 'not_exist':
        print('  PRODUTO NÃO ENCONTRADO')
    elif loja_1['status'] == 'not_available':
        print('  PRODUTO SEM ESTOQUE')
    else:
        print('  ESTOQUE: ' + loja_1['stock'])

    print('Loja 2')
    if loja_2['status'] == 'not_exist':
        print('  PRODUTO NÃO ENCONTRADO')
    elif loja_2['status'] == 'not_available':
        print('  PRODUTO SEM ESTOQUE')
    else:
        print('  ESTOQUE: ' + loja_2['stock'])

    print('Loja 3')
    if loja_3['status'] == 'not_exist':
        print('  PRODUTO NÃO ENCONTRADO')
    elif loja_3['status'] == 'not_available':
        print('  PRODUTO SEM ESTOQUE')
    else:
        print('  ESTOQUE: ' + loja_3['stock'])

    print('---> ESTOQUE TOTAL: ' + str(stock_total) + " <---")


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
while True:
    product_id = input()
    message = {
        'product': product_id
    }
    data = json.dumps(message)
    print("Consultando estoque das lojas...")
    tcp.sendall(bytes(data, encoding="UTF-8"))
    message = tcp.recv(1024)
    message = message.decode("UTF-8")
    parsed_data = json.loads(message)

    showResult(parsed_data, product_id)
