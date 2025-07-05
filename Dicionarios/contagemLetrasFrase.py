frase = input().split()
frase_unida = "".join(frase)
frase_unida_M = frase_unida.upper()

letras = "aáéíóúbcdefghijklmnopqrstuvwxyz".upper()
dic_letras = {} #caractere : contagem

caracteres_ordenados = sorted(frase_unida_M)


for caractere in caracteres_ordenados: # ! a a a r r // r
  if caractere in letras: # a a a r r  // r r
    contagem_caractere = caracteres_ordenados.count(caractere) # contagem_caractere = 3 // contagem_caractere = 2
    dic_letras[caractere] = contagem_caractere # a = 3 
  else:
    continue    

print(dic_letras)