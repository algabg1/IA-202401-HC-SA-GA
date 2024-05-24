# Manipulação de dados
import numpy as np
# Geração de números aleatórios
import random
import math
# Geração de gráficos
from matplotlib import pyplot as plt
from IPython.display import clear_output

import auxiliar as aux

def acceptance_probability(conflito_atual, novo_conflito, temperatura):
    if novo_conflito < conflito_atual: # melhor == menor (<)
        return 1.0
    else:
        return math.exp((conflito_atual - novo_conflito) / temperatura)
    
# SIMULATED ANNEALING
'''
def SimulatedAnnealing():
    s0 = solucaoInicial()
    T = 100
    while T > eps:
        s = estadoVizinhoAleatorio(s0)
        if f(s) > f(s0):
            s0 = s
        else:
            if random() <= exp((f(s)-f(s0))/T):
                s0 = s
        T = reduz(T)
'''

# nrep: número de vizinhos gerados em cada iteração
def simulated_annealing(tabuleiro, decaimento, iteracoes, nrep=50):

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
            novo_tabuleiro = aux.gera_vizinhos(tabuleiro_atual)
            novo_conflito = aux.conta_ataques(novo_tabuleiro)

            aceitacao_prob = acceptance_probability(conflito_atual, novo_conflito, temperatura)

            if random.random() < aceitacao_prob:
                tabuleiro_atual = novo_tabuleiro
                conflito_atual = novo_conflito

        temperatura *= decaimento

        #-----------------------------------------------
        if novo_conflito < lista_melhor_conflitos:
            melhor_tabuleiro = novo_tabuleiro
            lista_melhor_conflitos = novo_conflito

        lista_iteracoes += [iteracao]
        lista_melhor_conflitos += [lista_melhor_conflitos]
        lista_conflitos  += [conflito_atual]
        lista_aceitacao_prob  += [aceitacao_prob]
        lista_temperatura  += [temperatura]

        if iteracao % 50 == 0:
            print(f"Iteration {iteracao}, Best Conflicts: {lista_melhor_conflitos}")

        #-----------------------------------------------

    return melhor_tabuleiro, lista_melhor_conflitos

'''
initial_board = [random.randint(0, 7) for _ in range(8)]
initial_temperature = 1000
cooling_rate = 0.95
iterations = 1000

best_board, best_conflicts = simulated_annealing(initial_board, initial_temperature, cooling_rate, iterations)

print("Best board:", best_board)
print("Best conflicts:", best_conflicts)
'''