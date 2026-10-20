#Categorias 
idade = int(input("Digite a idade do nadador: "))

if idade <5:
    print("Não há categoria para essa idade")
elif idade <=7:
    print("Infantil A")
elif idade <=11:
    print("Infantil B")
elif idade <=13:
    print("Juvenil A")
elif idade <= 17:
    print("Juvenil B")
else: 
    print("Adulto")