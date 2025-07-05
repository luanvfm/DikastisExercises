palavras = []
vogais = "aeiouAEIOU"

palavra = input()
palavras = []
consoantes = []


while palavra != "fim":
    palavras.append(palavra)
    palavra = input()

for palavra in palavras:
    if palavra[0] not in vogais:
        consoantes.append(palavra)
        print(palavra)
    else:
        continue

if consoantes == []:
    print("Nenhuma palavra digitada começa com consoante.")
