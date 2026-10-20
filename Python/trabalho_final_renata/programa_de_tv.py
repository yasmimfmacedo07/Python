programas = []
canais = []
horarios = []
while True:
    print("Programa de TV")
    print("Menu:")
    print("1. Cadastrar nomes de programas, canais e horários")
    print("2. Pesquisar dados")
    print("3. Alterar dados ")
    print("4 - Remover opções")
    print("5 - Lista")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()
    if not opcao.isdigit():
        print("Opção inválida. Digite um número.")
        continue
    opcao = int(opcao)

    if opcao == 1:
        print(" === CADASTRO === ")
        while True:
            nome = input("Programa: ").strip().capitalize()
            if nome.isdigit() or not nome:
                print("Dado inválido. Digite o nome do programa novamente.")
            else:
                break
        programas.append(nome)

        while True:
            canal_str = input("Canal: ").strip()
            if not canal_str.isdigit():
                print("Dado inválido. Digite o número do canal novamente.")
            else:
                canal = int(canal_str)
                break
        canais.append(canal)

        while True:
            horario_str = input("Horário: ").strip()
            horario_com_pontos = f"{horario_str[:2]}:{horario_str[2:]}"
            print(horario_com_pontos)
            if not horario_str.isdigit():
                print("Dado inválido. Digite o horário novamente.")
            else:
                horario = int(horario_str)
                break
        horarios.append(horario)

        print(f"Dados cadastrados: {nome}, {canal}, {horario_com_pontos}")
        print("Cadastro realizado com sucesso!")

    elif opcao == 2:
        print("=== PESQUISAR DADOS ===")
        print("1. Nome do programa")
        print("2. Canal")
        print("3. Horário")
        pesquisa = input("Escolha uma opção: ").strip()
        if not pesquisa.isdigit():
            print("Opção inválida. Digite um número.")
            continue
        pesquisa = int(pesquisa)

        if pesquisa == 1:
            try:
                nome_pesquisa = input("Digite o nome do programa para pesquisar: ").strip().capitalize()
                posicao_programa = programas.index(nome)
                print(f"O {programas[posicao_programa]} passa no canal {canais[posicao_programa]} no horário {horarios[posicao_programa]}.")
            except ValueError:
                print("Programa não encontrado.")

        elif pesquisa == 2:
            try:
                canal_pesquisa = int(input("Digite o número do canal para pesquisar: ").strip())
                posicao_canal = canais.index(canal_pesquisa)
                print(f"O canal {canais[posicao_canal]} passa no horário {horarios[posicao_canal]}.")
            except ValueError:
                print("Canal não encontrado.")

        elif pesquisa == 3:
            try:
                horario_pesquisa = int(input("Digite o horário para pesquisar: ").strip())
                posicao_horario = horarios.index(horario_pesquisa)
                print(f"Horário {horarios[posicao_horario]} encontrado para o programa {programas[posicao_horario]} no canal {canais[posicao_horario]}.")
            except ValueError:
                print("Horário não encontrado.")
        else:
            print("Nenhum registro encontrado")
                
    elif opcao == 3:
        print("=== ALTERAR DADOS ===")
        print("1. Alterar nome de programa")
        print("2. Alterar Canal")
        print("3. Alterar horário")
        alterar = input("Escolha uma opção para fazer uma alteração: ").strip()
        if not alterar.isdigit():
            print("Opção inválida. Digite um número.")
            continue
        alterar = int(alterar)
        if alterar == 1:
            try:
                nome_antigo = input("Digite o nome do programa que deseja alterar: ").strip().capitalize()
                posicao_alterar = programas.index(nome_antigo)
                novo_nome = input("Digite o novo nome do programa: ").strip().capitalize()
                programas[posicao_alterar] = novo_nome
                print(f"Programa alterado de {nome_antigo} para {novo_nome}.")
            except ValueError:
                print("Programa não encontrado, tente novamente")
        elif alterar == 2:
            try:
                canal_antigo = int(input("Digite o número do canal que deseja alterar: ").strip())
                posicao_alterar = canais.index(canal_antigo)
                novo_canal = int(input("Digite o novo número do canal: ").strip())
                canais[posicao_alterar] = novo_canal
                print(f"Canal alterado de {canal_antigo} para {novo_canal}.")
            except ValueError:
                print("Canal não encontrado, tente novamente")
        elif alterar == 3:
            try:
                horario_antigo = int(input("Digite o horário que deseja alterar: ").strip())
                posicao_alterar = horarios.index(horario_antigo)
                novo_horario = int(input("Digite o novo horário: ").strip())
                horarios[posicao_alterar] = novo_horario
                print(f"Horário alterado de {horario_antigo} para {novo_horario}.")
            except ValueError:
                print("Horário inválido, tente novamente")
        else:
            print("Digite uma opção válida!")

    elif opcao == 4:
        print("=== REMOVER DADOS ===")
        print("1. Remover nome de programa")
        print("2. Remover Canal")
        print("3. Remover horário")
        remover = input("Escolha uma opção para remover: ").strip()
        if not remover.isdigit():
            print("Opção inválida. Digite um número.")
            continue
        remover = int(remover)

        if remover == 1:
            try:
                nome_remover = input("Digite o nome do programa que deseja remover: ").strip().capitalize()
                posicao_remover = programas.index(nome_remover)
                programas.pop(posicao_remover)
                canais.pop(posicao_remover)
                horarios.pop(posicao_remover)
                print(f"Programa {nome_remover} removido com sucesso.")
            except ValueError:
                print("Programa não encontrado, tente novamente")
        elif remover == 2:
            try:
                canal_remover = int(input("Digite o número do canal que deseja remover: ").strip())
                posicao_remover = canais.index(canal_remover)
                programas.pop(posicao_remover)
                canais.pop(posicao_remover)
                horarios.pop(posicao_remover)
                print(f"Canal {canal_remover} removido com sucesso.")
            except ValueError:
                print("Canal não encontrado, tente novamente")
        elif remover == 3:
            try:
                horario_remover = int(input("Digite o número do horário que deseja remover: ").strip())
                posicao_remover = horarios.index(horario_remover)
                programas.pop(posicao_remover)
                canais.pop(posicao_remover)
                horarios.pop(posicao_remover)
                print(f"Horário {horario_remover} removido com sucesso.")
            except ValueError:
                print("Horário inválido, tente novamente")
        else:
            print("Opção inválida, tente novamente")

    elif opcao == 5:
        print("=== LISTA ===")
        for i in range (len(programas)):
            print(f"Programa: {programas[i]}, Canal: {canais[i]}, Horário: {horarios[i]}")
    elif opcao == 0:
        print("Sair")
        break
    else:
        print("Nenhuma opção válida digitada")