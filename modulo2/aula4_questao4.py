# Entrada de dados
valor = int (input("Digite o valor: "))

# Processamento de dados 
#### Contagem das notas - maior para menor
notas_100 = valor // 100
valor = valor % 100 #### Atualização do restante do valor

notas_50 = valor // 50
valor = valor % 50 #### Atualização do restante do valor

notas_20 = valor // 20
valor = valor % 20 #### Atualização do restante do valor

notas_10 = valor // 10
valor = valor % 10 #### Atualização do restante do valor

notas_5 = valor // 5
valor = valor % 5 #### Atualização do restante do valor

notas_2 = valor // 2
valor = valor % 2 #### Atualização do restante do valor

notas_1 = valor // 1
valor = valor % 1 #### Atualização do restante do valor

# Saída de dados
print (f"{notas_100} nota(s) de R$ 100,00")
print (f"{notas_50} nota(s) de R$ 50,00")
print (f"{notas_20} nota(s) de R$ 20,00")
print (f"{notas_10} nota(s) de R$ 10,00")
print (f"{notas_5} nota(s) de R$ 5,00")
print (f"{notas_2} nota(s) de R$ 2,00")
print (f"{notas_1} nota(s) de R$ 1,00")