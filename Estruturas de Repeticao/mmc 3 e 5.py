n = int(input())
contador = 0

while contador <= n:
    if contador % 3 == 0 and contador % 5 != 0:
        print(f"{contador} é múltiplo de 3")
    
    elif contador % 5 == 0 and contador % 3 != 0:
        print(f"{contador} é múltiplo de 5")
    
    elif contador % 3 == 0 and contador % 5 == 0:
        print(f"{contador} é múltiplo de 3 e de 5")

    contador += 1