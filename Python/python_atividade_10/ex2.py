filmes_em_cartaz = ["Batman", "Matrix", "Avatar"]
while True:
    print("-------------------------")
    print("----🐍CINEMA PYTHON🐍---- ")
    print("-------------------------")
    print(f"Filmes disponíveis em cartaz: {filmes_em_cartaz}")
    print("--- MENU PRINCIPAL ---")
    print("-----------------------")
    print("1 - Adicionar um nome filme")
    print("2 - Remover um filme")
    print("3 - Procurar a posição do filme")
    print("4 - para sair")
    print("----------------------")
    opcao = int(input("Digite a ação desejada (1, 2, 3 ou 4): "))
    if opcao == 1:
        novo_filme = input("Digite o nome do filme desejado: ").capitalize()
        filmes_em_cartaz.append(novo_filme)
        print(f"Filme adicionado: {novo_filme}")
        print()
    elif opcao == 2:
        retirar_filme = input("Informe o nome do filme que deseja retirar: ").capitalize()
        try:
            filmes_em_cartaz.remove(retirar_filme)
            print(f"Filme removido: {retirar_filme}")
            print()
        except ValueError:
            print("O filme não existe na lista")
            print()

    elif opcao == 3:
        buscar_filme = input("Qual filme está procurando? ").capitalize()
        try:
            posicao = filmes_em_cartaz.index(buscar_filme)
            print(f"A posição do filme é: {posicao}")
            print()
        except ValueError:
            print("O filme não existe na lista")
            print()
    else: 
        print(f"A lista atualizada de filmes: {filmes_em_cartaz}")
        print("Saindo do sistema")
        print()
        break