paciente = input("Digite o nome do paciente:")
peso = float(input("Digite o peso do paciente em kg: "))
altura = float(input("Digite a altura do paciente em metros: "))

# Cálculo do IMC 
imc = peso / (altura * altura)

if imc < 20:
   print(f"Paciente {paciente}, sua faixa de risco é: Abaixo do peso")
elif imc <=25:
   print(f"Paciente {paciente}, sua faixa de risco é:Normal")
elif imc <= 35:
   print(f"Paciente {paciente}, sua faixa de risco é: Excesso de peso")
elif imc <= 50:
   print(f"Paciente {paciente}, sua faixa de risco é:Obesidade")
else:
   print(f"Paciente {paciente}, sua faixa de risco é:Obesidade mórbida")