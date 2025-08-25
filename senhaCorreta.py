# -*- coding: utf-8 -*-

def verificar_senha():
    """
    Solicita a senha ao usuário e verifica se está correta,
    com um limite de 5 tentativas.
    """
    # Defina a senha correta que o sistema deve esperar.
    # Por segurança, em um sistema real, isso nunca seria armazenado diretamente no código.
    senha_correta = "FedGalactica2025"

    # Inicializa o contador de tentativas. O usuário tem 5 chances.
    tentativas_maximas = 5
    tentativas_feitas = 0

    print("--- Controle de Acesso da Federação Galáctica ---")

    # O loop continua enquanto o usuário não tiver esgotado suas tentativas.
    while tentativas_feitas < tentativas_maximas:
        try:
            # Solicita que o usuário insira a senha.
            senha_digitada = input("Por favor, digite sua senha: ")

            # 1. Verifica se a senha digitada é a correta.
            if senha_digitada == senha_correta:
                print("\n✅ Acesso concedido! Bem-vindo(a) ao sistema.")
                # Se a senha estiver correta, interrompe o loop.
                return  # Encerra a função com sucesso.
            else:
                # 2. Se a senha estiver incorreta, informa o usuário.
                tentativas_feitas += 1
                tentativas_restantes = tentativas_maximas - tentativas_feitas

                # Informa quantas tentativas ainda restam, se houver alguma.
                if tentativas_restantes > 0:
                    # Mensagem de erro amigável.
                    print(f"❌ Senha incorreta. Você tem mais {tentativas_restantes} tentativa(s).")

        except KeyboardInterrupt:
            # Lida com o caso de o usuário pressionar Ctrl+C para sair.
            print("\nOperação cancelada pelo usuário.")
            return

    # 3. Se o loop terminar sem que a senha correta seja inserida,
    # significa que o usuário esgotou todas as tentativas.
    print("\n🚫 Conta bloqueada! Você excedeu o número máximo de tentativas.")


# --- Ponto de entrada do programa ---
if __name__ == "__main__":
    verificar_senha()
