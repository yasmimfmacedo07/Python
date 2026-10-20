total_aprovados = total_reprovados = soma_geral_das_medias = 0
TOTAL_ALUNOS = 3 # tamanho
for i in range(TOTAL_ALUNOS):
    matricula = int(input("Digite a matrícula do aluno: "))
    nota1 = float(input("Digite o valor da nota 1 do aluno: "))
    nota2 = float(input("Digite o valor da nota 2 do aluno: "))
    media = (nota1 + nota2)/2
    if media > 5:
        print(f"Aluno com matrícula {matricula} está aprovado com {media}")
        total_aprovados += 1
    else:
        print(f"Aluno com matrícula {matricula} está reprovado com {media}")
        total_reprovados += 1
    soma_geral_das_medias += media
print("--- Resumo da turma ---")
print(f"O total de alunos aprovados é: {total_aprovados}")
print(f"O total de alunos reprovados é: {total_reprovados}")
print(f"Média geral da turma: {soma_geral_das_medias/TOTAL_ALUNOS}")