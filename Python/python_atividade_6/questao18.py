salario = float(input("Qual o seu salário: "))
financiamento = float(input("Qual o valor do financiamento?: "))

if financiamento <= salario * 5:
    print("Financiamento concedido")
else:
    print("Financiamento não concedido")
print("Obrigado por nos consultar")