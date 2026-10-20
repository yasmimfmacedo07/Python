soma = total_valores = quant_positivos = quant_negativos = 0
while True:
    numero = int(input("Digite um valor (0 para finalizar):"))
    if numero == 0:
        break
    soma += numero
    total_valores += 1
    if numero > 0:
        quant_positivos += 1
    else:
        quant_negativos += 1 
if total_valores > 0:
    print(f"A média dos valores: {soma/total_valores}")
    print(f"A quantidade de valores positivos é: {quant_positivos}")
    percentual = (quant_negativos * 100)/total_valores
    print(f"O percentual de números negativos é de {percentual}%")
else:
    print("Não foi digitado nenhum valor.")