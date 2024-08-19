# Usuário insere a temperatura em Fahrenheit (jeito errado, todo mundo sabe)
temperatura_jeito_errado = float (input("Digite a temperatura em graus Fahrenheit: "))

# Fórmula de conversão
temperatura_jeito_certo = int ((temperatura_jeito_errado - 32) * ( 5 / 9))

# Impressão final
print (f"{temperatura_jeito_errado} graus Fahrenheit são {temperatura_jeito_certo} graus Celsius")