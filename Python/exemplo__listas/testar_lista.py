alunos = []
for i in range(5):
    alunos.append(input(f"Digite o nome {i+1}° aluno: "))
print(alunos)
alunos.extend(["mario", "sebastiao"])
print("Depois do extend", alunos)
alunos.sort()
print("Depois do sort", alunos)