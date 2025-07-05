valor_total = 0

for i in range(4):
    nome = input()
    quantidade = int(input())
    preco_unitario = float(input())
    total = quantidade * preco_unitario
    valor_total = total + valor_total
    print(f"{nome} - {quantidade} unidades - R$ {preco_unitario:.2f} cada - Total: R$ {total:.2f}")
print("")
print(f"Valor total do estoque: R$ {valor_total}")