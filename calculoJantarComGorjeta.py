# --- Cálculo de Jantar com Gorjeta ---

# 1. Entrada de dados
valor_conta = float(input("Qual o valor da conta do jantar? R$ "))
percentual_gorjeta = float(input("Qual a porcentagem de gorjeta que deseja dar (ex: 10)? "))

# 2. Processamento
valor_gorjeta = valor_conta * (percentual_gorjeta / 100)
valor_total_jantar = valor_conta + valor_gorjeta

# 3. Saída de dados
print("\n--- Resumo da Conta ---")
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Valor da gorjeta ({percentual_gorjeta}%): R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {valor_total_jantar:.2f}")