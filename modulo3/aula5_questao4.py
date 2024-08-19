# Entrada de dados
classe = (input("Digite sua classe (guerreiro, mago ou arqueiro): "))
força = int (input("Qual o valor de Força do seu personagem? "))
magia = int (input("Qual o valor de Magia do seu personagem? "))

# Processamento e saída de dados
if classe == "guerreiro" and força >= 15 and magia <= 10:
            print(True)
elif classe == "mago" and força <= 10 and magia >= 15:
            print(True)
elif classe == "arqueiro" and 5 < força <= 15 and 5 < magia <= 15:
            print(True)
