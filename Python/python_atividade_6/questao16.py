numero = int(input("Digite um número inteiro: "))

# Verficar se o numero informado é múltiplo e divisivel por 3 e por 7 ao mesmo tempo    

if numero %3 == 0 and numero %7 == 0:
        print(f"O némero {numero} é divisivel por 3 e por 7.")
else: 
    print(f"O número {numero} não é divisivel nem por 3 e 7.") 
