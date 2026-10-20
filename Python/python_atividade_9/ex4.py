numeros = []
for i in range(5):
    numeros.append(int(input("Digite um número da posição 0: ")))

maior = max(numeros)
posicao = numeros.index(maior)
print(f"O índice do maior número é: {maior}")
print(f"O maior número da lista é {maior} e está na posição {posicao}")