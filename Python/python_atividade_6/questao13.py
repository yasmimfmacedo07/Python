valorHoraAula = float(input("Digite o valor da hora-aula: "))
aulasDadas = int(input("Digite a quantidade de aulas dadas: "))
descontoINSS = float(input("Digite o percentual de desconto do INSS: "))

salarioBruto = valorHoraAula * aulasDadas                               # Sem desconto
salarioLiquido = salarioBruto - (salarioBruto * descontoINSS)/100       # Com desconto
print(f"Seu salário líquido é: R$ {salarioLiquido}")

if salarioLiquido > (1412 * 10):
    print("Parabéns pelo seu esforço!")
elif salarioLiquido > (1412 * 6):
    print(f"Um dia você chega lá!")
else:
    print("Ah! Precisa se esforçar!")