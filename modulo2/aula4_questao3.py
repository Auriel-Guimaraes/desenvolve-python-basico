# Inserção de dados (Entrada)
produto_1 = (input("Digite o nome do produto 1: "))
valor_produto_1 = float(input(f"Digite o preço unitário do produto {produto_1}: "))
quantidade_produto_1 = int (input(f"Digite a quantidade unitária do produto {produto_1}: "))

produto_2 = (input("Digite o nome do produto 2: "))
valor_produto_2 = float(input(f"Digite o preço unitário do produto {produto_2}: "))
quantidade_produto_2 = int (input(f"Digite a quantidade unitária do produto {produto_2}: "))

produto_3 = (input("Digite o nome do produto 3: "))
valor_produto_3 = float(input(f"Digite o preço unitário do produto {produto_3}: "))
quantidade_produto_3 = int (input(f"Digite a quantidade unitária do produto {produto_3}: "))

# Processamento e Saída de Dados
print (f"O valor total da compra é de R$ {quantidade_produto_1 * valor_produto_1 + quantidade_produto_2 * valor_produto_2 + quantidade_produto_3 * valor_produto_3:,.2f}")