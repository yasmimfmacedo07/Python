#Caminhos para a aprovação do aluno
media = float(input("Digite a média final do aluno: "))
faltas = int(input("Digite o número de faltas: "))

# Situação atual do aluno com base nas notas e faltas
if media >= 7 and faltas < 32:
    print("Aprovado") 
elif media < 7 and faltas < 32:
    print("Reprovado por média")
elif media >= 7 and faltas >= 32:
    print("Reprovado por falta")
else:
    print("Reprovado por média e por falta")
