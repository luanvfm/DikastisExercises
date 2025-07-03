saldo = float(input())
saldo_anterior = saldo
operacao = ""

while operacao != "sair":
  operacao = input()
  if operacao == "depositar":
    deposito = float(input())
    saldo_atual = saldo_anterior + deposito
    saldo_anterior = saldo_atual
    continue
  elif operacao == "sacar":
    saque = float(input())
    saldo_atual = saldo_anterior - saque
    saldo_anterior = saldo_atual
    continue




print(f"Seu saldo era: R$ {saldo:.2f}")
print(f"Seu novo saldo é: R$ {saldo_atual:.2f}")