confirmacao = "s"
total_n = []
ja_impresso = []

while confirmacao == "s" or confirmacao == "S":
  n = float(input())
  total_n.append(n)
  
  confirmacao = input()
  

#vou usar index e cont 
for numero in total_n:
  if numero not in ja_impresso:
    n_contado = total_n.count(numero)
    print(f"O elemento {numero} aparece {n_contado} vezes na lista ")
    ja_impresso.append(numero)
  else:
    continue
  