idade = int(input())
cnh = int(input())

if cnh == 0 and idade < 18:
    print("Você ainda não pode dirigir.")
elif cnh == 1 and idade < 18:
    print("Como você tem menos de 18 anos e pode dirigir? Alô, Polícia!!!")
elif cnh == 1 and idade > 18:
    print("Você pode dirigir. Dirija com segurança!!")
elif cnh == 0 and idade > 18:
    print("Você pode tirar a CNH e dirigir.")