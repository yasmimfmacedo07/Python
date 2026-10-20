soma_alturas = acima_160 = abaixo_130 = 0
maior = 0 
menor = 9999
TAMANHO = 3
for i in range(TAMANHO):
    altura = float(input("Digite a altura da pessoa: "))
    if altura > maior:
        maior = altura
    if altura < menor:  
        menor = altura
    soma_alturas += altura
    if altura > 1.60: 
        acima_160 += 1
    if altura < 1.30:
        abaixo_130 += 1
print(f"Maior altura: {maior:.2f}")
print(f"Menor altura: {menor:.2f}")
print(f"Média das alturas: {soma_alturas/TAMANHO:.2f}")
print(f"Pessoas mais altas que 1.60m: {acima_160}")
print(f"Pessoas mais baixas que 1.30m: {abaixo_130}")
