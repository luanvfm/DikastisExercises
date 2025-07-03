
nomes = []
notas = []
nome_aluno = input("Digite o nome do aluno ou \"fim\" para terminar o programa: ")   


while nome_aluno != "" and nome_aluno != "fim":
        
    nomes.append(nome_aluno)    

    nota_aluno = float(input("Digite a nota do aluno: "))
    notas.append(nota_aluno)
    
    nome_aluno = input("Digite o nome do aluno ou \"fim\" para terminar o programa: ")
    
lista = list(zip(notas, nomes))
lista_ordenada = sorted(lista, reverse=True)

for item in lista_ordenada:
    nome_aluno = item[1]
    nota_aluno = item[0]

    print(f"{nome_aluno}: {nota_aluno:.2f}")