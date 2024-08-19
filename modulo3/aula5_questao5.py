# Entrada de dados
genero =    (input("Digite seu gênero (M ou F): "))
idade = int (input("Digite sua idade: "))
tempo = int (input("Digite seu tempo de serviço: "))

# Processamento de dados
a = (genero == 'F' and idade >= 60) or (genero == 'M' and idade >= 65)
b = tempo > 30
c = (idade >= 60 and tempo >= 25)

pode_aposentar = a or b or c 

# Saída de dados
print (pode_aposentar)