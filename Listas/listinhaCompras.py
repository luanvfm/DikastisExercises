item = input()

comprinhas = []

while item != "fim":
  comprinhas.append(item)
  item = input()
  
comprinhas.sort()

print(*comprinhas, sep="\n")