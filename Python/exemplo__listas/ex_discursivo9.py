mamiferos = ["vaca", "cabra", "ovelha", "capivara", "gato"]
try:
    indice = mamiferos.index("cavalo")
    print(indice)
except:
    print("Cavalo não encontrado na lista de mamíferos.")