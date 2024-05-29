# Geração de números aleatórios
import random

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

# Seleciona melhor vizinho
def obtem_melhor_vizinho(tabuleiro, solucao_inicial):
    melhor_custo = conta_ataques(solucao_inicial) #solucao aleatoria que foi criada
    melhor_vizinho = solucao_inicial

    for vizinho in gera_vizinhos(solucao_inicial):
        custo_atual = conta_ataques(vizinho)
        if custo_atual < melhor_custo:
            melhor_custo = custo_atual
            melhor_vizinho = vizinho

    return melhor_vizinho, melhor_custo

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
def conta_ataques(VT): # função-objetivo o número de pares de rainhas se atacando
    ataques  = __conta_ataques_linhas(VT)
    ataques += __conta_ataques_diagonais(VT)

    return ataques

# Gera tuplas com os custos de todos os individuos da populacao | Função fitness
def gera_tuplas_custos(Populacao):

    TuplasCustos = []
    for individuo in Populacao:
        ataques = conta_ataques(individuo)

        TuplasCustos += [(ataques, individuo)]

    return TuplasCustos

# Cria uma solucao inicial com as rainhas em um ordem aleatoria
def solucao_aleatoria():
    return random.sample(range(8), 8)