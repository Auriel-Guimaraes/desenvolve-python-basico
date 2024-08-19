#Entrada de dados
idade = int (input("Digite sua idade: "))
jogos = int (input("Quantos jogos de tabuleiro você já jogou? "))
vitoria = int (input("Quantos vezes você venceu um jogo de tabuleiro? "))

# Processamento 
pode_participar = (idade >= 16 and idade <= 18) and (jogos >= 3) and (vitoria >= 1)

# Saída de dados
print (pode_participar)
