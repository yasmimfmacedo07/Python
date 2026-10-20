preco_livro = 39.90
qtd_livros_comprados = int(input("Quantos livros você está comprando? "))
if qtd_livros_comprados >= 4:
    desconto = 18
else:
    desconto = 8
valor_total = preco_livro * qtd_livros_comprados
valor_total_desconto = valor_total - (valor_total * (desconto/100))
print(f"Valor total sem desconto: R${valor_total:.2f}")
print(f"Valor total com desconto: R${valor_total_desconto:.2f}")