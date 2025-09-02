# --- Conversão de Dólares para Reais ---

# 1. Entrada de dados
valor_em_dolares = float(input("Digite o valor da compra em dólares (ex: 50.25): $ "))
cotacao_dolar = float(input("Digite a cotação atual do dólar (ex: 5.15): "))

# 2. Processamento
valor_em_reais = valor_em_dolares * cotacao_dolar

# 3. Saída de dados
print(f"O valor equivalente em reais é: R$ {valor_em_reais:.2f}")