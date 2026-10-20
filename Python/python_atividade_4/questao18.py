cotacao = float(input("Digite a cotação do dólar (R$ por US$): "))
reais = float(input("Digite quantos Reais (R$) você tem para converter: "))

dolares = reais / cotacao

print(f"Você levará ${dolares:.2f}")