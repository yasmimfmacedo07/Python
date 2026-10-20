salario_bruto = float(input("Informe o salário bruto: "))
valor_prestacao = float(input("Informe o valor da prestação: "))

limite = salario_bruto * 0.30
if valor_prestacao <= limite:
    print(f"Empréstimo CONCEDIDO. O limite de 30% é R$ {limite:.2f}.")
else:
    print(f"Empréstimo NEGADO. A prestação de R$ {valor_prestacao:.2f} excede o limite de R$ {limite:.2f}.")
