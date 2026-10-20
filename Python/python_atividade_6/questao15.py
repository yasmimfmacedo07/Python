#Identificar segmentos de reta que podem formar um triângulo 
lado_a = float(input("Digite o lado A:"))
lado_b = float(input("Digite o lado B:"))
lado_c = float(input("Digite o lado C:"))

if lado_a <= 0 or lado_b <= 0 or lado_c <=0:
    print("Os valores informados não podem formar um triângulo.")
elif lado_a >= (lado_b + lado_c) or lado_b >= (lado_a + lado_c) or lado_c >= (lado_a + lado_b):
    print("Os valores informados não podem formar um triângulo.")
elif lado_a == lado_b == lado_c:
    print("Os lados informados formam um triângulo equilátero.")
elif lado_a != lado_b != lado_c:
    print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados forma um triângulo isósceles.")