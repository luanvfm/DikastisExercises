numeros = []

for i in range(10):
  numero = float(input())
  numeros.append(numero)

expoente = int(input())

for numero in numeros:
  resultado = numero ** expoente
  print(f"{resultado:.2f}")