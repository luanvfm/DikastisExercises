n = int(input())

#numero inicial
# soma
# se a soma for maior que o numero inicial vai parar.
a = 0
b = 1
proximo_numero = int
fibolista = []
fibo = 0

while fibo <= n:
  proximo_numero = a + b # 1 + 1 = 2
  a = b # a = 1
  b = a + proximo_numero # b = 1 + 2
  
  fibolista.append(b)
  fibo = b

print(*fibolista, sep="\n")