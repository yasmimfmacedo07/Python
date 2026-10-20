'''                                 x = salario + (salario * percentual)/100) = 1000 + (1000*10)/100 = 1100
Aumentar      percentual 1.15       salario + salario * 0.15 = 1150 
                                    ou 
                                    salario * 1.15 = 1000 * 1.15 = 1150
,.
Diminuir      percentual 0.15      salario - salario * 0.15 = 1000-150 = 850
                                    ou 
                                    salario * 0.85 = 850
'''

salario_atual = float(input("Digite o valor do salário atual: "))

if salario_atual <= 500:
    reajuste = salario_atual * 1.15
elif salario_atual <= 1000:
    reajuste = salario_atual * 1.10
else:
    reajuste = salario_atual * 1.05
print(f"O novo salário será de: R$ {reajuste}")