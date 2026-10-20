listaA = [10,5,2]
listaB = [8,9,2]
listaC = []
for i in range(3):
    if listaA[i] > listaB[i]:
        listaC.append(listaA[i] - listaB[i])
    else:
        listaC.append(listaB[i] - listaA[i])
print(listaC)