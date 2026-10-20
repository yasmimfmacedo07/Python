total_folha = num_empregados = 0
while True: 
    matricula = int(input("Digite o número da matríula (Digite 0 sair): "))
    if matricula == 0:
        break
    salario_dia = float(input("Salário por dia: "))
    dias_trabalhados = int(input("Dias trabalhados: "))
    salario = salario_dia * dias_trabalhados
    print(f"Empregado {matricula}: Salário = R$ {salario}")
    total_folha += salario
    num_empregados += 1

print("--- Resumo da folha ---")
print(f"O total da folha de pagamento é: {total_folha}")
print(f"A média salarial: R$ {total_folha / num_empregados}")