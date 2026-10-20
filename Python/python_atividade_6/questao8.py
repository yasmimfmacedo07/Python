f1 = int(input("Digite a pontuação do primeiro finalista: "))
f2 = int(input("Digite a pontuação do segundo finalista: "))
f3 = int(input("Digite a pontuação do terceiro finalista: "))
print("Pódio")

# Análise do primeiro, segundo e terceiro lugar
if f1 > f2 > f3:
    print(f"1º Lugar: {f1} pontos")
    print(f"2º Lugar: {f2} pontos")
    print(f"3º Lugar: {f3} pontos") 
elif f1 > f3 > f2:
    print(f"1º Lugar: {f1} pontos")
    print(f"2º Lugar: {f3} pontos")
    print(f"3º Lugar: {f2} pontos") 
elif f2 > f1 > f3:
    print(f"1º Lugar: {f2} pontos")
    print(f"2º Lugar: {f1} pontos")
    print(f"3º Lugar: {f3} pontos") 
elif f2 > f3 >f1:
    print(f"1º Lugar: {f2} pontos")
    print(f"2º Lugar: {f3} pontos")
    print(f"3º Lugar: {f1} pontos") 
elif f3 > f1 > f2:
    print(f"1º Lugar: {f3} pontos")
    print(f"2º Lugar: {f1} pontos")
    print(f"3º Lugar: {f2} pontos") 
elif f3 > f2 > f1:
    print(f"1º Lugar: {f3} pontos")
    print(f"2º Lugar: {f2} pontos")
    print(f"3º Lugar: {f1} pontos") 
else:
    print(f"1º Lugar: {f3} pontos")
    print(f"2º Lugar: {f2} pontos")
    print(f"3º Lugar: {f1} pontos") 