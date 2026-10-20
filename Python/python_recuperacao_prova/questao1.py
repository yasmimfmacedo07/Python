qtd_clientes_mais_60 = qtd_alunos = soma_peso = num_cliente = 0
clientes = 6
for i in range(clientes):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    peso = float(input("Digite o peso do aluno: "))
    num_cliente += 1
    if idade >= 60:
        qtd_clientes_mais_60 += 1
    print(f"Cliente {num_cliente}: nome: {nome}, idade: {idade}, peso: {peso}")
media_peso = soma_peso + peso
print(f"Média de peso do grupo: {media_peso} kg")
print(f"Quantidade de clientes acima de 60 anos: {qtd_clientes_mais_60}")
