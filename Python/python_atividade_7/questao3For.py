soma = 0
for i in range (3):
    numero = int(input("Digite um número: "))
    resto = numero %3
    soma += resto
print(f"A soma dos restos é: {soma}")