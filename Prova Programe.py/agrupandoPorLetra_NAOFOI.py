nome = input()
nomes =[]
inicial = []

dicionario = {}

while nome != "fim": #Input inicial dos nomes
    nomes.append(nome)    
    nome = input()
    if dicionario[letra]:
        dicionario[letra].append(nome)
    

# {
#     "A": ['ana', 'Amanda'],
#     B: ["bruno", "beto"]
# }


for nome in nomes: #Gera lista de iniciais
    inicial_nome = nome[0]
    inicial.append(inicial_nome)

nomes_maiusculos = nome.upper() #Iniciais em ordem alfabetica
inicial = inicial

for letra, nome in inicial, nomes:
    if letra == nomes_maiusculos[0]:
        dicionario[letra] = nome
    else:
        continue

print(dicionario)
# for nome in nomes:
#     if inicial == inicial_nome


