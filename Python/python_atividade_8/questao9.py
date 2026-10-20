soma_idades = idade_mais_velha = 0
nome_mais_velha = mulheres_jovens = ""
for i in range(4):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Informe o sexo ('M' para masculino e 'F' para feminino): ").upper()
    soma_idades += idade
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velha = nome
    if sexo == "F" and idade < 20:
        mulheres_jovens += nome + "|"
    print(f"A média de idade do grupo é de: {soma_idades / 4} anos")
    print(f"Pessoa mais velha do grupo é: {nome_mais_velha}, com {idade_mais_velha} anos")
    print(f"Mulheres com menos de 20 anos: {mulheres_jovens}")