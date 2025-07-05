n = int(input())


while n != 1:
    if n % 2 == 0: # par
        n = (n*3)+1
        print(n)
    else:
        n = n // 2   # impar 
        print(n)
