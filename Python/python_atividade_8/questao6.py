maior_altura = mulheres_altas = soma_altura_mulheres30 = cont_mulheres30 = 0
TOTAL_PESSOAS = 3
for i in range (TOTAL_PESSOAS):
    altura = float(input("Digite a altura da pessoa: "))
    sexo = input("Informe o sexo (M para masculino e F para feminino): ")
    idade = int(input("Digite a idade da pessoa: "))
    if altura > maior_altura:
        maior_altura = altura
    if sexo == "F" and altura >= 1.70:
        mulheres_altas += 1
    if sexo == "F" and idade > 30:
        soma_altura_mulheres30 += altura
        cont_mulheres30 += 1
print(f"A maior altura do grupo é : {maior_altura}")
print(f"Número de mulheres com altura maior ou igual a 1.70: {mulheres_altas}")
if cont_mulheres30 > 0:
    print(f"A média de altura das mulheres com mais de 30 anos é de: {soma_altura_mulheres30/cont_mulheres30}")
else:
    print("Não tem mulheres acima de 30 anos")