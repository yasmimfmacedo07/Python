fruta = []
for i in range(3):
    fruta.append(input("Digite o nome de três frutas vermelhas: "))

frutas = []
for i in range(2):
    frutas.append(input("Quais são as suas frutas favoritas? "))

print(fruta)
fruta.extend([frutas])
print(frutas)
print(fruta)
