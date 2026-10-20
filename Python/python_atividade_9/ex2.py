listaA = []
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        listaA.append(numero)
        print("Adicionado")
    else:
        print("Ignorado")
        
print(f"A listaA é:{listaA} ")

listaB = [numero ** 3 for numero in listaA]
print(f"A lista com os números ao cubo é: {listaB}")