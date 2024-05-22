# HILL-CLIMBING COM RESTART
def hill_climbing_restart(tsp):

    for _ in range(50):

        # solucao inicial
        solucao_inicial = solucao_aleatoria(tsp)
        # melhor solucao ate o momento
        solucao_melhor, custo_melhor = obtem_melhor_vizinho(tsp, solucao_inicial)

        while True:

            # tenta obter um candidato melhor
            candidato_atual, custo_atual = obtem_melhor_vizinho(tsp, solucao_melhor)
            #print(custo_melhor, custo_atual)

            if custo_atual < custo_melhor:
                custo_melhor   = custo_atual
                solucao_melhor = candidato_atual
            else:
                break   # custo nao melhorou, entao sai do while

    return custo_melhor, solucao_melhor