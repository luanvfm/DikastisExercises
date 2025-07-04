#ESSE ARQUIVO SERVE PARA COLOCAR CODIGOS CORRIGIDOS E COMPARAR COM O MEU
n = int(input())

a, b = 0, 1 
a, b = b, a + b

while a <= n:
    print(a)
    a, b = b, a + b