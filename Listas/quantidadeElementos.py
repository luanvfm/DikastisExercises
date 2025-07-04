confirmacao = "s"
total_n = []


while confirmacao == "s" or confirmacao == "S":
  n = float(input())
  total_n.append(n)
  
  confirmacao = input()
  

#vou usar index e cont 
for numero in total_n:
  n_contado = total_n.count(numero)
  print(f"O elemento {numero} aparece {n_contado} vezes na lista ")
  