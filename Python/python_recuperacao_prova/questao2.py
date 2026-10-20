durabilidade = 0
while True:
    lampada = int(input("Digite a durabilidade da lâmpada (ou 0 para sair): "))
    if lampada == 0:
        break
    if durabilidade < lampada:
        lampada += durabilidade
print(f"Menor tempo de durabilidade registrado: {lampada}")
