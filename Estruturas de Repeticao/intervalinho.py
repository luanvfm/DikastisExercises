primeiro = int(input())
segundo = int(input())
soma = primeiro + segundo
contador = primeiro

pares = []
impares = []


print(f"A soma dos números é: {soma} \n")

if segundo >= primeiro:
  
  while contador <= segundo:
    if contador % 2 == 0:
      pares.append(contador)
    elif contador % 2 != 0:
      impares.append(contador)
    
    contador += 1
  
print("Os números pares dentro da sequência são:")
if pares:
  print(*pares, sep='\n')
print("")
print("Os números ímpares dentro da sequência são:")
if impares:
  print(*impares, sep='\n')
