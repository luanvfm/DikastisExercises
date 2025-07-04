palavra = input()

palavras = []

while palavra != "fim":
  palavras.append(palavra)
  palavra = input()



busca_vogais = []

for item in palavras:
  separador = item[0].lower()
  if separador == "a" or separador == "e" or separador == "i" or separador =="o" or separador == "u":
    busca_vogais.append(item)
  else:
    continue


if busca_vogais:
  print(*busca_vogais, sep="\n")
else:
  print("Nenhuma palavra digitada começa com vogal.")

# MEU ERRO FOI O SEGUINTE:

# o metodo split() separa as palavras automaticamente de acordo com algo entre elas
# por padrao esse algo é o espaço. 

# como nao tinha espaço nenhum na palavra "abacaxi", ele retornava a propria palavra.
# dessa forma abacaxi era sempre != de "a".

# entao quando voce usa a propria lista do item, ele ja automaticamente pega os index do item. nao precisa do split. nao sei se deu p entender mas foi isso

# ##
# Outra forma de resolver a comparacao que ficou meio feia era utilizando o método "in"

# Cria uma variavel com as vogais que quero comparar. vogais = "aeiou"
# e depois comparo
# if separador in vogais:
#   busca_vogais.append(item)
# else...