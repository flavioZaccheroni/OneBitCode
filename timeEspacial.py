def montar_times_espaciais(astronautas: list[dict]) -> int:
    """
    Calcula a quantidade máxima de times espaciais que podem ser formados.

    Args:
        astronautas: Uma lista de dicionários, onde cada dicionário representa
                     um astronauta com seu nome e uma lista de habilidades.

    Returns:
        O número inteiro da quantidade máxima de times completos.
    """
    habilidades_da_missao = ["Piloto", "Engenheiro", "Médico", "Cientista"]

    # Fazemos uma cópia da lista para poder remover astronautas sem alterar a original
    astronautas_disponiveis = list(astronautas)
    times_formados = 0

    while True:
        habilidades_necessarias = set(habilidades_da_missao)
        indices_dos_astronautas_usados = []

        # Tenta montar um time, buscando preencher as habilidades necessárias
        for i, astronauta in enumerate(astronautas_disponiveis):
            habilidades_do_candidato = set(astronauta["habilidades"])

            # Verifica se o candidato tem alguma habilidade que ainda precisamos
            habilidades_em_comum = habilidades_necessarias.intersection(habilidades_do_candidato)

            if habilidades_em_comum:
                # Se sim, "recruta" o astronauta para este time
                indices_dos_astronautas_usados.append(i)
                # Remove as habilidades que ele cobre da nossa lista de necessidades
                habilidades_necessarias -= habilidades_em_comum

            # Se já cobrimos todas as habilidades, podemos parar de procurar para este time
            if not habilidades_necessarias:
                break

        # Se, após a busca, conseguimos cobrir todas as habilidades, o time é válido
        if not habilidades_necessarias:
            times_formados += 1

            # Remove os astronautas usados do pool de disponíveis para a próxima iteração.
            # É importante remover pelos maiores índices primeiro para não bagunçar a lista.
            for i in sorted(indices_dos_astronautas_usados, reverse=True):
                astronautas_disponiveis.pop(i)
        else:
            # Se não foi possível formar um time completo com os astronautas restantes, paramos o processo.
            break

    return times_formados


# --- Exemplo de Uso ---
if __name__ == "__main__":
    astronautas_exemplo = [
        {"nome": "Alice", "habilidades": ["Piloto", "Engenheiro"]},
        {"nome": "Bob", "habilidades": ["Médico"]},
        {"nome": "Charlie", "habilidades": ["Cientista", "Engenheiro"]},
        {"nome": "Diana", "habilidades": ["Piloto", "Médico", "Cientista"]}
    ]

    quantidade_de_times = montar_times_espaciais(astronautas_exemplo)

    print(f"🚀 Análise de Recrutamento da Federação Galáctica 🚀")
    print("-" * 50)
    print(f"Astronautas candidatos: {len(astronautas_exemplo)}")
    print(f"Resultado: É possível formar {quantidade_de_times} time(s) completo(s).")
    print("-" * 50)