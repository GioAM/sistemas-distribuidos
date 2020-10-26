# Sistemas Distribuídos
 Atividades desenvolvidas durante as aulas de Sistemas Distribuídos
 
 --------------------
## Trabalho consulta-estoque
### Linguagem Utilizada: 
 - Python
 
### Pacotes: 
- Socket
- JSON
- CSV

### Atores
 - Servidores: Servem para consultar os estoques das lojas em uma planilha no formato .csv.
 - Servente: Recebe a requisição do cliente e solicita para todos os servidores, cada um se referindo a uma loja diferente.
 - Cliente: Recebe por meio do console o id do produto e solicita ao servidor o estoque daquele produto.

### Execução
Para o funcionamento correto do sistema bem como a conexão entre os servidores o usuário deve rodar os programas nessa ordem:
Servidores -> Servente -> Cliente

### Funcionamento
No programa Cliente o usuário irá digitar o id do produto, que será enviado com um formato json para o servente que repassa para todos os servidor. Cada servidor retorna um json de resposta contendo o status do produto, o estoque e o nome da loja. Na saída é mostrado para o cliente os resultados recebidos.
