n = int(input())
i = 1
dic = {}

for i in range(1, n+1):
  dic[i] = i*i

for chave, valor in dic.items():
    print(f"{chave}: {valor}")

