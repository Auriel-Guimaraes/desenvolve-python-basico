# Solicita ao usuário a distância em quilômetros e o peso do pacote em quilogramas
distancia = float(input("Insira a distância da entrega em quilômetros: "))
peso = float(input("Insira o peso do pacote em quilogramas: "))

# Calcula o valor base do frete com base na distância
if distancia <= 100:
    valor_frete = peso * 1  # R$1 por kg
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50  # R$1.50 por kg
else:
    valor_frete = peso * 2  # R$2 por kg

# Adiciona uma taxa adicional de R$10 se o peso for superior a 10 kg
if peso > 10:
    valor_frete += 10

# Imprime o valor final do frete
print(f"O valor do frete é: R${valor_frete:.2f}")