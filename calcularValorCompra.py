# --- Cálculo do Valor Total de uma Compra ---

# 1. Entrada de dados
preco_produto1 = float(input("Digite o preço do primeiro produto: R$ "))
preco_produto2 = float(input("Digite o preço do segundo produto: R$ "))
preco_produto3 = float(input("Digite o preço do terceiro produto: R$ "))

# 2. Processamento
valor_total = preco_produto1 + preco_produto2 + preco_produto3

# 3. Saída de dados
# O ":.2f" formata o número para exibir sempre duas casas decimais.
print(f"O valor total da sua compra é: R$ {valor_total:.2f}")