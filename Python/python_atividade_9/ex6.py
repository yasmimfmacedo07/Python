nomes = []
quantidades = []
precos = []
for i in range(3):
    nomes.append(input(f"Digite o nome do {i+1}º produto: "))
    quantidades.append(int(input(f"Digite a quantidade do {i+1}º produto: ")))
    precos.append(float(input(f"Digite o primeiro preço do {i+1} produto: ")))

# Calcular o faturamento
faturamentoTotal = 0
for i in range(len(nomes)):
    faturamento = quantidades[i] * precos[i]
    print(f"Faturamento do {nomes[i]}: R$ {faturamento:.2f}")           #i é de índice
    faturamentoTotal += faturamento

print(f"Faturamento TOTAL da loja: R$ {faturamentoTotal:.2f} ")