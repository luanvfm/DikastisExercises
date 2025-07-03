saldo = float(input("Digite seu saldo: "))
saldo_anterior = saldo
operacao = ""

while operacao != "sair":
  operacao = input("depositar, sacar ou sair? ")
  if operacao == "depositar":
    deposito = float(input("Insira o valor do deposito: "))
    saldo_atual = saldo_anterior + deposito
    saldo_anterior = saldo_atual
    continue
  elif operacao == "sacar":
    saque = float(input("Insira o valor do seu saque: "))
    saldo_atual = saldo_anterior - saque
    saldo_anterior = saldo_atual
    continue




print(f"Seu saldo era: R$ {saldo:.2f}")
print(f"Seu novo saldo é: R$ {saldo_atual:.2f}")