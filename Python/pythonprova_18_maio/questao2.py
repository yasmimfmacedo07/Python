maior_peso = 0
while True:
    peso = float(input("Digite o peso do atleta (ou 0 para sair): "))
    if peso == 0:
        break
    if peso > maior_peso:
        maior_peso = peso 
print(f"Maior peso informado: {maior_peso:.2f}")