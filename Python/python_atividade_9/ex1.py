numero = []
for i in range(5):
    numero.append(int(input("Digite um número: ")))
print(numero)

soma = [0]
soma = sum(numero)
print(soma)
print(f"A soma total dos números é {soma}")