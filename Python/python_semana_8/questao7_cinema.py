#Programa para calcular o faturamento diário de um cinema com a venda de ingressos

#Preços dos ingressos 
preco_ingresso_adultos = 30.00
preco_ingresso_idosos = 20.00

#Solicitar ao usuário que digite a quantidade de ingressos vendidos por categoria (adultos e idosos)
adultos = int(input("Digite a quantidade de ingressos vendidos para adultos: "))
idosos = int(input("Digite a quantidade de ingressos vendidos para idosos: "))
categoriaAdultos = (adultos * 30)
categoriaIdosos= ( idosos * 20)
totalVendas = categoriaAdultos + categoriaIdosos 

print(f"Faturamento da categoria adultos: ", categoriaAdultos)
print(f"Faturamento da categoria idosos: ", categoriaIdosos)
print(f"O total de faturamento do dia foi de", totalVendas)