# Usuário irá inserir o comprimento do terreno
comprimento = int (input("Digite o comprimento do terreno: "))
# Usuário irá inserir a largura do terreno
largura = int (input("Digite a largura do terreno: "))
# Usuário irá inserir o valor do metro quadrado do terreno
valor_m2 = float (input("Digite o valor do metro²: "))

# Fórmula da área total
area_m2 = comprimento * largura
# Fórmula do preço total
preço_total = area_m2 * valor_m2

# Impressão final
print (f"O terreno possui {area_m2} m² e custa R$ {preço_total:,.2f}")