peso = float(input("Insira o seu peso em KG: "))
altura = float(input("Insira a sua altura em metros: ")) 

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")