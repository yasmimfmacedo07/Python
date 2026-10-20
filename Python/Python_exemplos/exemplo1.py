#Entrada de dados
'''
nome = input("Digite seu nome: ") #str
sobrenome = input("Digite seu sobrenome: ") #str
dade = int(input("Digite sua idade: "))   #str
ano = 2026              #int
salario = 2000.52        #float
'''  
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

#processamento
soma = numero1 + numero2

#saída de dados
'''
print("Olá",nome,sobrenome, "!")
print("Sua idade é", idade, "anos.")
print("em", ano, "meu salário é R$", salario)
'''
print("A soma é", soma)
print("A soma é "+ str (soma))
print(f"A soma é {soma}")

print("A soma de", numero1, "+", numero2, "=", soma)
print("A soma de ", str(numero1) + "+" + str(numero2) + "=" + str(soma))
print(f"A soma {numero1} + {numero2} = {soma}")
print("A soma de {} + {} = {}". format(numero1, numero2, soma))
