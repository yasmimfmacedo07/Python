# Sequência de Fibonacci é a soma dos dois números interiores
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a = 0
b = 1
for i in range(a,n):
    print(a)
    c = a + b
    a = b 
    b = c 