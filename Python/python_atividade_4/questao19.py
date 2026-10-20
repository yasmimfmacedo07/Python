nomeVendedor = input("Digite o nome do vendedor: ")
salarioFixo = float(input("Digite o salário fixo do vendedor R$: "))
totalVendas = float(input("Digite o total de vendas efetuadas pelo vendedor por mes em R$: "))

comissao = (totalVendas*15)/100

print(f"{nomeVendedor} tem salário fixo igual a {salarioFixo}")
print(f"Seu salário final é de {salarioFixo+comissao}")