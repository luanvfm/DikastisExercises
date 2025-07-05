capital = float(input())
taxa = float(input())
tempo = int(input())

taxa_juros = taxa / 100

juros = capital * taxa_juros * tempo

print(f"O total alcançado é de R${juros:.2f} ao final dos {tempo} meses.")