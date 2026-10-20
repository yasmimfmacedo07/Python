cand1 = cand2 = cand3 = brancos = nulos = 0
while True:
    voto = int(input("Digite seu voto (1,2,3,0,4 ou -1) para encerrar: "))
    if voto == -1:
        break 
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 +=1
    elif voto == 3:
        cand3 += 1
    elif voto == 0:
        brancos += 1
    elif voto == 4:
        nulos += 1
    else:
        print("Voto inválido. Tente novamente.")
total_votos = cand1 + cand2 + cand3 + brancos + nulos
if total_votos > 0:
    if cand1 > cand2 and cand1 > cand3:
        print(f"O vencedor é o candidato 1 com {cand1} votos")
    elif cand2 > cand1 and cand2 > cand3:
        print(f"O vencedor é o candidato 2 com {cand2} votos")
    else:
        print(f"O vencedor é o candidato 3 com {cand3} votos")
    print(f"Total de votos em branco: {brancos}")
    print(f"Total de votos nulos: {nulos}")
    print(f"Total de eleitores: {total_votos}")
else:
    print("Não foi digitado nenhum voto válido.")