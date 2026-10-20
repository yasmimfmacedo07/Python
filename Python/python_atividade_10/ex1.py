lista_compras = []
for i in range(3):
    lista_compras.append(input(f"Qual é o {i+1}º item da lista? "))
print(f"Os itens na lista de compras são: {lista_compras}")

try:
    item = input("Digite o nome do produto que deseja remover: ")
    posicao = lista_compras.index(item)
    lista_compras.remove(item)
    print(f"O produto: {item} foi removido e ele estava na posição: {posicao}")
except ValueError:
    print("Ops! Esse item não foi encontrado na lista")