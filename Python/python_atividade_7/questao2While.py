numero = int(input("Digite um número inteiro positivo: "))
soma = 0    #Acumuladora
cont = 1    # Contadora

while cont <= numero:
    soma += cont
    cont += 1 
print(f"A soma de 1 até {numero} é: {soma}")
