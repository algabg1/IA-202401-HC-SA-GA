# Funções auxiliares genéricas aos problemas
import auxiliar as aux

# HILL-CLIMBING COM RESTART
def hill_climbing_restart(tabuleiro):
    print("Tabuleiro recebido:", tabuleiro)
    # Parâmetro: 20 restarts
    for _ in range(20):
        print("Iteração", _+1)
        # solucao inicial
        solucao_inicial = aux.solucao_aleatoria()
        print("Solução gerada aleatoriamente:", solucao_inicial)
        # melhor solucao ate o momento
        solucao_melhor, custo_melhor = aux.obtem_melhor_vizinho(tabuleiro, solucao_inicial)
        print("Melhor solução até o momento:", solucao_melhor, "com custo", custo_melhor)
        while True:
            # tenta obter um candidato melhor
            candidato_atual, custo_atual = aux.obtem_melhor_vizinho(tabuleiro, solucao_melhor)
            # print(custo_melhor, custo_atual)
            if custo_atual < custo_melhor:
                custo_melhor   = custo_atual
                solucao_melhor = candidato_atual
            else:
                break   # custo nao melhorou, entao sai do while

    return custo_melhor, solucao_melhor

def main():
    vetor = [4,8,2,7,3,7,5,4]
    custo, vetor_melhor = (hill_climbing_restart(vetor))
    print("Melhor solução:", vetor_melhor, "com custo:", custo)
    print("TABULEIRO\n", aux.converte_tabuleiro(vetor_melhor)) # melhorar converte_tabuleiro pra ficar mais visual

if __name__ == '__main__':
    main()