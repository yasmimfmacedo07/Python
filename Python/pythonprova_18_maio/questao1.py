homens_mais_25 = soma_idades = num_aluno = 0
qtd_alunos = 5
for i in range(qtd_alunos):
    num_aluno += 1
    nome = input("Digite o sue nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = input("Informe o seu sexo (F para feminino e M para masculino): ").upper()
    soma_idades += idade 
    
    if sexo == 'M' and idade > 25:
        homens_mais_25 += 1
    print(f"Aluno {num_aluno}: Nome = {nome}, idade = {idade}, sexo = {sexo}")
media_idade = soma_idades / qtd_alunos
print(f"Média de idade do grupo: {media_idade}")
print(f"Homens com mais de 25 anos: {homens_mais_25}")