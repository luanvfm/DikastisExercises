nome_telefone = input()
nomes_e_telefones = {}


while nome_telefone != "fim":
    nome, telefone = nome_telefone.split() # Ana 1248
    nomeMin = nome.lower()
    nomes_e_telefones[nomeMin] = telefone
    nome_telefone = input()
    # nomes_e_telefones.append(nome_telefone)

consulta_nome = input()
comparador_nome = consulta_nome.lower()


if comparador_nome in nomes_e_telefones.keys():
    print(nomes_e_telefones.get(comparador_nome))
else:
    print("Essa pessoa não está na lista telefônica")