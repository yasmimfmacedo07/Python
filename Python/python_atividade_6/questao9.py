nome_aluno = input("Digite o nome do aluno: ")
nota_trabalho = float(input("Digite a nota do trabalho: "))
nota_prova = float(input("Digite a nota da prova:"))

#Situação do aluno: Aprovado ou reprovado

media = (nota_trabalho + nota_prova)/2
print("Valor da média é:", media)

if media >=7:
    print(f"{nome_aluno} está com a situação: Aprovado")
else:
    print(f"{nome_aluno} está com a situação: Reprovado")
