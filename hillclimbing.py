# Manipulação de dados
import numpy as np
import pandas as pd
# Geração de números aleatórios
import random
from math import sqrt
# Geração de gráficos
from matplotlib import pyplot as plt
import seaborn as sns
from plotly import express as px
from plotly import graph_objects as go
from IPython.display import clear_output

import auxiliar as aux

# FUNÇÕES AUXILIARES PARA HC

# Cria uma solucao inicial com as cidades em um ordem aleatoria
def solucao_aleatoria():
    return random.sample(range(8), 8)

# Seleciona melhor vizinho
def obtem_melhor_vizinho(tabuleiro, solucao_inicial):
    melhor_custo = aux.conta_ataques(solucao_inicial) #solucao aleatoria que foi criada
    melhor_vizinho = solucao_inicial

    for vizinho in aux.gera_vizinhos(solucao_inicial):
        custo_atual = aux.conta_ataques(vizinho)
        if custo_atual < melhor_custo:
            melhor_custo = custo_atual
            melhor_vizinho = vizinho

    return melhor_vizinho, melhor_custo

# HILL-CLIMBING COM RESTART
def hill_climbing_restart(tabuleiro):
    # Parâmetro: 20 restarts
    for _ in range(20):
        # solucao inicial
        solucao_inicial = solucao_aleatoria()
        # melhor solucao ate o momento
        solucao_melhor, custo_melhor = obtem_melhor_vizinho(tabuleiro, solucao_inicial)

        while True:
            # tenta obter um candidato melhor
            candidato_atual, custo_atual = obtem_melhor_vizinho(tabuleiro, solucao_melhor)
            #print(custo_melhor, custo_atual)
            if custo_atual < custo_melhor:
                custo_melhor   = custo_atual
                solucao_melhor = candidato_atual
            else:
                break   # custo nao melhorou, entao sai do while

    return custo_melhor, solucao_melhor