lista_elementos = input().split() #1 2 1 1 3 4
contador = 0

lista_numeros = []

for element in lista_elementos:
  numero_convertido = int(element)
  lista_numeros.append(numero_convertido)

  

soma_elementos = sum(lista_numeros) #12

divisor_aritmetico = len(lista_numeros) #6

media_aritmetica = soma_elementos / divisor_aritmetico #12 / 6 e isso vai ser 2. veja os numeros maiores que 2

lista_final = []

for item in lista_numeros:
  if item > media_aritmetica:
    contador += 1 
  else:
    continue 

print(contador)