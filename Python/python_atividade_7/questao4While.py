soma = 0 
cont = 0
while True:
    numero = int(input("Digite um número ou -1 para sair: "))
    if numero == -1:
        break
    soma += numero
    cont += 1
if cont > 0: 
    media = soma / cont
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum úmero foi digitado")
