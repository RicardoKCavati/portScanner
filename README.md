# Experiência Finger Print (NMAP + Python)
## Experiência realizada para a disciplina Planejamento e Implementação de Serviços em Redes de Computadores (SEGMA4 - 2023)
### Professor: 
DR. FÁBIO HENRIQUE CABRINI
### Alunos: 
BRENO AUGUSTO BATISTA GIANOTTI

RICARDO KROMER CAVATI
## Explicação sobre o código linha a linha
Nas três primeiras linhas são importadas as bibliotecas usadas no experimento, são elas nmap, socket e typing
Da linha 5 a linha 23 é definida uma classe chamada Scanner, ela é composta por duas propriedades, a "canConnect" usada para identificar se é possível se conectar a determinada porta, a porta é definida na propriedade "port", na classe há quatro métodos (getters e settters) e um construtor.

Na linha 25 é definida a variável target com o valor "127.0.0.1", é o localhost, ip que vai ter as portas validadas.

Na linha 27 é criada a variável portScanner por meio do nmap.portScanner(), está variável é usada para fazer a validação das portas.
Na linha 29 é criada uma variável chamada fiwareScanners, ela é um vetor do tipo Scanner (previamente criado), em que cada uma das instâncias da classe recebe uma das portas que o software fiware abre, preenchendo a propriedade "port" com o número da porta e a propriedade "canConnect" como False.

A partir da linha 31 é iniciado um laço que vai passar por cada um dos elementos de fiwareScanners.

A linha 32 faz a impressão da mensagem "testing port: ", seguida do número da porta que será testada.

A linha 33 faz a chamada do método scan, que recebe dois parâmetros, o alvo, que neste caso é a variável target, e qual a porta que será analisada, o resultado é salvo na variável result, o conteúdo é um json (JavaScript Object Notation).

A linha 34 faz a conversão de result buscando o estado da porta específica no ip específico, este resultado sobrescreve a variável result, e o valor dela agora pode ser 'open', 'closed', 'filtered', 'unfiltered' ou 'open|filtered' (https://nmap.org/book/man-port-scanning-basics.html).

Na linha 35 verificamos se o valor de result é 'open', se for o caso, a propriedade canConnect do scanner atual será preenchida na linha 36 com True.

Na linha 37 há um else, quer dizer que se a variável não tiver o valor de 'open', o valor da propriedade canConnect do scanner atual será preenchido na linha 38 como False.

Na linha 41, é validado se todos os itens da lista fiwareScanners tem a propriedade canConnect como True, se for o caso, será exibida a mensagem na linha 42 que o fiware está instalado e em execução.

Na linha 43 há um else, ou seja, se pelo menos um dos scanners de fiwareScanners tiver a propriedade canConnect como False, será exibida na linha 44 uma mensagem dizendo que o fiware não está em execução.