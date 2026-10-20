# Verificar se um participante tem a idade correta para se inscrever em um evento juvenil

#  idades entre 10 e 18 anos
idade = int(input("Digite a sua idade: "))

if 10 <= idade <= 18:
    print("Idade válida para o evento.")
else:
    print("Idade não válida para o evento.")