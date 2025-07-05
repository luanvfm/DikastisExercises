n = int(input())
reprovados = []
nome_aluno = input()
nota_aluno = float(input())

def alunos_abaixo_da_media(nome_aluno, nota_aluno):   
    if nota_aluno < 7:
        reprovados.append(nome_aluno)


for i in range(n-1): # 0 1 2
    alunos_abaixo_da_media(nome_aluno, nota_aluno)
    nome_aluno = input()
    nota_aluno = float(input())

print("Os alunos que reprovaram foram: ")
print(*reprovados, sep="\n")
