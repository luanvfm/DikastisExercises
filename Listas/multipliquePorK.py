elementos = input().split()
multiplicador = int(input())

elementos_inteiros = []
lista_multiplicados = []

for element in elementos:
  elemento_int = int(element)
  elementos_inteiros.append(elemento_int)
  
# lista de elementos inteiros = elementos_inteiros

for element in elementos_inteiros:
  elementoMultiplicado = element * multiplicador
  lista_multiplicados.append(elementoMultiplicado)
# elementos multiplicados sao mandados para a lista_multiplicados

print(*lista_multiplicados)
  