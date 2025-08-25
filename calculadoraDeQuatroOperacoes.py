# -*- coding: utf-8 -*-

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Calculadora Python ---")
    print("Escolha uma operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Sair")
    print("--------------------------")


def calculadora():
    """
    Função principal que opera a calculadora, exibindo um menu
    e realizando cálculos com base na escolha do usuário.
    """
    # O loop infinito mantém o programa em execução até que o usuário escolha sair.
    while True:
        exibir_menu()

        # Pede ao usuário para escolher uma opção do menu.
        escolha = input("Digite o número da sua opção: ")

        # --- Verificação da Escolha do Usuário ---

        # 1. Verifica se o usuário quer sair do programa.
        if escolha == '5':
            print("\nObrigado por usar a calculadora. Até logo! 👋")
            break  # Interrompe o loop e encerra o programa.

        # 2. Verifica se a escolha é uma das operações válidas.
        if escolha in ['1', '2', '3', '4']:
            try:
                # Pede os dois números para o cálculo.
                # Usamos float() para permitir números com casas decimais.
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                # Se o usuário digitar algo que não seja um número (ex: "abc"),
                # exibe uma mensagem de erro e volta ao início do loop.
                print("\n❌ Erro: Por favor, insira apenas números.")
                continue  # Pula para a próxima iteração do loop.

            # --- Realiza o Cálculo com Base na Escolha ---

            resultado = 0
            if escolha == '1':
                resultado = num1 + num2
                print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")

            elif escolha == '2':
                resultado = num1 - num2
                print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")

            elif escolha == '3':
                resultado = num1 * num2
                print(f"\n✅ Resultado: {num1} * {num2} = {resultado}")

            elif escolha == '4':
                # Tratamento especial para o caso de divisão por zero.
                if num2 == 0:
                    print("\n❌ Erro: Não é possível dividir por zero.")
                else:
                    resultado = num1 / num2
                    print(f"\n✅ Resultado: {num1} / {num2} = {resultado}")

        else:
            # 3. Se a escolha não for nenhuma das opções válidas.
            print("\n❌ Opção inválida. Por favor, escolha um número de 1 a 5.")


# --- Ponto de Entrada do Programa ---
# A linha abaixo garante que a função calculadora() só seja executada
# quando o script é rodado diretamente.
if __name__ == "__main__":
    calculadora()
