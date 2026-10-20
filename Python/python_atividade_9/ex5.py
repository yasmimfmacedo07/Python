letras = ['P', 'Y', 'T', 'T', 'H', 'O', 'N', 'N', 'N', 'S']
cont = 0
# Letra A
for i in range(len(letras)):
    if letras[i] == 'A':
        cont += 1

if cont == 0:
    print("A letra 'A' não foi encontrada.")
else:
    print(f"Tem {cont} letras 'A' na lista")

# Letra B
cont = 0
pares = []
for i in range(len(letras)-1):
    if letras[i] == letras[i+1]:
        pares.append(letras[i]+letras[i+1])
        cont += 1
print(f"Total de pares sequenciais: {cont}")
print(f"Pares encontrados: {pares}")