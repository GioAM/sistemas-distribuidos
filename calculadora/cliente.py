import socket, time
import random, json

operacoes = ['ADICAO', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO']
HOST = ''
PORT = 5555
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)
tcp.bind(origem)
tcp.listen(2)
con, cliente = tcp.accept()


def sortInfo():
    valor1 = input()
    if valor1 == "FIM":
        infoJson = {
            'operacao': "FIM"
        }
        return infoJson
    infoJson = {
        'valor1': int(valor1),
        'valor2': int(input()),
        'operacao': input()
    }
    return infoJson

while True:
    data = json.dumps(sortInfo())
    con.sendall(bytes(data, encoding="UTF-8"))
    mensagem = con.recv(1024)
    mensagem = mensagem.decode("UTF-8")
    parsed_data = json.loads(mensagem)
    time.sleep(1)
    print("resultado: " + str(parsed_data['resultado']))

