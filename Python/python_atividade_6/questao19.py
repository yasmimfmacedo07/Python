calcados = float(input("Quantos calçados você está comprando? "))
valor_total = calcados * 49.90
if calcados <= 2:
    valor_final = valor_total * 0.95
else:
    valor_final = valor_total * 0.85
print(f"Valor total sem desconto: {valor_total:.2f}")
print(f"Valor total com desconto: {valor_final:.2f}")