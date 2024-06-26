# Geração de números aleatórios
import random
import math
# Funções auxiliares genéricas aos problemas
import auxiliar as aux
import plotagem as graf

def probabilidade_aceitacao(conflito_atual, novo_conflito, temperatura):
    if novo_conflito < conflito_atual: # melhor == menor (<)
        return 1.0
    else:
        return math.exp((conflito_atual - novo_conflito) / temperatura)
    
# SIMULATED ANNEALING

# nrep: número de vizinhos gerados em cada iteração
def simulated_annealing(tabuleiro, nrep=50):
    decaimento_min = 0.1
    decaimento_max = 1
    iteracoes = 30
    
    tabuleiro_atual = tabuleiro.copy()
    melhor_tabuleiro = tabuleiro_atual.copy()
    
    conflito_atual = aux.conta_ataques(tabuleiro_atual)
    melhor_conflito = conflito_atual
    # Parâmetro: temperatura = 1000
    temperatura = 1000
    
    #-----------------------------------------------------
    lista_iteracoes = []
    lista_melhor_conflitos = []
    lista_conflitos = []
    lista_aceitacao_prob = []
    lista_temperatura = []
    #-----------------------------------------------------
    
    for iteracao in range(iteracoes):
        for _ in range(nrep):
            novo_tabuleiro, novo_conflito = aux.obtem_melhor_vizinho(tabuleiro_atual, melhor_tabuleiro)
            
            aceitacao_prob = probabilidade_aceitacao(conflito_atual, novo_conflito, temperatura)

            if random.random() < aceitacao_prob:
                tabuleiro_atual = novo_tabuleiro
                conflito_atual = novo_conflito

        decaimento = random.uniform(decaimento_min, decaimento_max)
        temperatura *= (1 - decaimento)

        #-----------------------------------------------
        if novo_conflito < melhor_conflito:
            melhor_tabuleiro = novo_tabuleiro
            melhor_conflito = novo_conflito

        lista_iteracoes += [iteracao]
        lista_melhor_conflitos += [melhor_conflito]
        lista_conflitos  += [conflito_atual]
        lista_aceitacao_prob  += [aceitacao_prob]
        lista_temperatura  += [temperatura]

        if iteracao % 50 == 0:
            print(f"Iteração {iteracao}, melhor conflito: {melhor_conflito}")
            graf.plot_axes_figure(lista_iteracoes, lista_aceitacao_prob, lista_temperatura)
        #-----------------------------------------------

    return melhor_conflito, melhor_tabuleiro

def main():
    vetor = [4,8,2,7,3,7,5,4]
    custo, vetor_melhor = (simulated_annealing(vetor,0.1,1,30))
    print("Melhor solução:", vetor_melhor, "com custo:", custo)
    print("TABULEIRO\n", aux.converte_tabuleiro(vetor_melhor)) # melhorar converte_tabuleiro pra ficar mais visual

if __name__ == '__main__':
    main()