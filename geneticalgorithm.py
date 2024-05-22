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

# Recebe um vetor representando um tabuleiro com N rainhas, uma por coluna e retorna uma lista de lista de 0 e 1 representando um tabuleiro com as rainhas.
def converte_tabuleiro(VT):

    N = len(VT)

    L = [0]*N
    T = []
    for i in range(N):
        T += [L.copy()]

    for lin in range(N):
        for col in range(N):
            if lin+1 == VT[col]:
                T[lin][col] = 1

    return T

# Função que recebe um Vetor-Tabuleiro e retorna o número de pares de rainhas se atacando mutuamente nas linhas.
def __conta_ataques_linhas(VT):

    ataques = 0
    N = len(VT)
    for col1 in range(N):
        lin1 = VT[col1]
        for col2 in range(col1+1, N):
            lin2 = VT[col2]
            if lin1==lin2:
                ataques +=1

    return ataques

# Função que recebe um Vetor-Tabuleiro e retorna o número de pares de rainhas se atacando mutuamente nas diagonais.
def __conta_ataques_diagonais(VT):
    
    ataques = 0
    N = len(VT)

    for col1 in range(N):
        lin1 = VT[col1]
        for col2 in range(col1+1, N):
            lin2 = VT[col2]

            # diferenças entre as linhas e colunas
            d1 = lin1-col1
            d2 = lin2-col2

            # somas das linhas e colunas
            s1 = lin1+col1
            s2 = lin2+col2

            # condições para ataques nas diagonais
            if d1==d2 or s1==s2:
                ataques +=1
                #print(f'({lin1},{col1+1}) ({lin2},{col2+1}) -->', ataques,
                #      '<--', f'  -({d1:2},{d2:2})  +({s1:2},{s2:2})')

    return ataques

# Função que recebe um Vetor-Tabuleiro e retorna o número de pares de rainhas se atacando mutuamente nas linhas e diagonais.
def conta_ataques(VT):

    ataques  = __conta_ataques_linhas(VT)

    ataques += __conta_ataques_diagonais(VT)

    return ataques

# Gera todos os vizinhos possíveis, variando uma rainha de cada vez.
def gera_vizinhos(VT):

    N = len(VT)
    for col in range(N):
        for lin in range(N):
            # se nao existe rainha naquela linha,
            # entao gera estado vizinho.
            linha = lin+1
            if linha != VT[col]:
                vizinho   = VT.copy()
                vizinho[col] = linha

                yield vizinho

# Gera tuplas com os custos de todos os individuos da populacao | Função fitness
def gera_tuplas_custos(Populacao):

    TuplasCustos = []
    for individuo in Populacao:
        ataques = conta_ataques(individuo)

        TuplasCustos += [(ataques, individuo)]

    return TuplasCustos

def mutacao(VT, p_mutacao=0.20):

    VT_mutated = VT.copy()

    N = len(VT)
    p = np.random.rand()

    if p < p_mutacao:
        col   = np.random.randint(0,N)    # indice da coluna (base-0)
        linha = np.random.randint(1,N+1)  # valor da linha   (base-1)

        VT_mutated[col] = linha
        #print(col+1, linha)

    return VT_mutated

# Crossover com dois vetores
def crossover2(Parent1, Parent2):

    N = len(Parent1)

    # ponto de corte
    c = np.random.randint(1, N-1)

    # crossover no ponto de corte
    # gerando dois filhos
    child1 = Parent1[:c] + Parent2[c:]      # Python List format
    child2 = Parent2[:c] + Parent1[c:]      # Python List format

    return child1, child2

# SELECAO POR TORNEIO
def selecao(Populacao):
    Candidato1 = random.choice(Populacao)
    Candidato2 = random.choice(Populacao)

    a1 = conta_ataques(Candidato1)
    a2 = conta_ataques(Candidato2)

    # eleito o candidato com menor custo
    eleito = Candidato1 if a1<=a2 else Candidato2

    return eleito

# individuo é um Vetor (N) em que cada posicação representa uma coluna indicando as respectivas linhas ocupadas pelas rainhas em um tabuleiro (NxN).
def gera_individuo(n_cols):
    # VT = [low, high) x n_cols

    VT = np.random.randint(low=1, high=n_cols+1, size=n_cols)
    return VT

# N: tamanho do tabuleiro (NxN)
# tam_pop: tamanho da população
def gera_populacao_inicial(N, tam_pop):

    populacao = []
    for _ in range(tam_pop):
        individuo = gera_individuo(N)

        populacao.append(individuo)

    return populacao

def algoritmo_genetico(N, tam_pop, num_geracoes):
    # Função fitness
    fitness = gera_tuplas_custos
    # Gera população inicial
    Populacao = gera_populacao_inicial(N, tam_pop)
    # Executa N gerações
    for geracao in range(num_geracoes):
        for i in range(tam_pop / 2):

            # Seleciona dois candidatos
            p1 = selecao(Populacao)
            p2 = selecao(Populacao)
            #     Crossover
            #     Mutation
            #     Compute fitness
            # ...
            # coloque seu código aqui
            #
    # ...
    # coloque seu código aqui
    pass

VT = np.array([4,8,2,7,3,7,5,4])
converte_tabuleiro(VT)
conta_ataques(VT)
Populacao = gera_vizinhos(VT) # <=== TROCAR P GERAR SOLUÇÕES ALEATORIAS; CHAMAR N VEZES P GERAR A POPULAÇÃO
Tuplas = gera_tuplas_custos(Populacao)
Tuplas
sorted(Tuplas, key=lambda k: k[0])
VT2 = mutacao(VT)
crossover2(VT,VT2)
selecao([VT,VT2])
N = 8
tam_pop = 20
Populacao = gera_populacao_inicial(N, tam_pop)
Populacao
gera_tuplas_custos(Populacao)