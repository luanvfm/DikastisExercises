n = int(input())
dicionario = {}

for i in range(n):
  categoria_valor = input().split()
  
  categoria = categoria_valor[0]
  valor_recebido = categoria_valor[1]
  valor_total = int(valor_recebido)
  if categoria in dicionario:
    dicionario[categoria] = dicionario[categoria] + valor_total
  else:
    dicionario.update({categoria : valor_total})

for key, value in dicionario.items():
  chave = key
  valor = value
  print(f"{chave}: {valor}")
  