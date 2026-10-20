limite = float(input("Qual o limite de peso de hoje (KG): "))
peso_total = 0
while True:
    peso = float(input("Peso do peixe (KG) ou 0 para finalizar: "))
    if peso == 0:
        break
    peso_total += peso 
    print(f"O peso total até agora; {peso_total} kg")
    if peso_total > limite:
        print(f"Limite de peso excedido!")
        break