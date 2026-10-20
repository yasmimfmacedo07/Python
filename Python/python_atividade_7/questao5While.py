while True:
    senha = input("Crie uma senha com 8 caracteres: ")
    if len(senha) >= 8:
        break
    print("Sua senha é muito curta. Tente novamente")
print("Senha cadastrada com sucesso!")