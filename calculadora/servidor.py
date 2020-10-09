import socket
import time
import sys, json

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.249.1'
port = 5555
destino = (host, port)
tcp.connect(destino)


def calcular(data):
    resultado = 0
    parsed_data = json.loads(data)
    if parsed_data['operacao'] == "FIM":
        print("OPERACAO FINALIZADA")
        sys.exit()
    valor1 = parsed_data['valor1']
    valor2 = parsed_data['valor2']
    if parsed_data['operacao'] == 'ADICAO':
        resultado = valor1 + valor2
    elif parsed_data['operacao'] == 'SUBTRACAO':
        resultado = valor1 - valor2
    elif parsed_data['operacao'] == 'DIVISAO':
        resultado= valor1/valor2
    elif parsed_data['operacao'] == 'MULTIPLICACAO':
        resultado = valor1 * valor2
    else:
        resultado = "OPERACAO NAO IDENTIFICADA"
    result = {
        'resultado': resultado
    }
    return result


while True:
    mensagem = tcp.recv(1024)
    mensagem = mensagem.decode("UTF-8")
    print("recebido: " + mensagem)
    time.sleep(1)
    data = json.dumps(calcular(mensagem))
    tcp.sendall(bytes(data, encoding="UTF-8"))
