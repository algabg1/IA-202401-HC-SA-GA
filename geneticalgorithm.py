# Manipulação de dados
import numpy as np
# Geração de números aleatórios
import random
# Funções auxiliares genéricas aos problemas
import auxiliar as aux

# Gera tuplas com os custos de todos os individuos da populacao | Função fitness
def gera_tuplas_custos(Populacao):

    TuplasCustos = []
    for individuo in Populacao:
        ataques = aux.conta_ataques(individuo)

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

    a1 = aux.conta_ataques(Candidato1)
    a2 = aux.conta_ataques(Candidato2)

    # eleito o candidato com menor custo
    eleito = Candidato1 if a1<=a2 else Candidato2

    return eleito

# individuo é um Vetor (N) em que cada posicação representa uma coluna indicando as respectivas linhas ocupadas pelas rainhas em um tabuleiro (NxN).
def gera_individuo(n_cols):
    # VT = [low, high) x n_cols

    VT = np.random.randint(low=1, high=n_cols+1, size=n_cols)
    return VT

# N: tamanho do tabuleiro (NxN) | tam_pop: tamanho da população
def gera_populacao_inicial(N, tam_pop):

    populacao = []
    for _ in range(tam_pop):
        individuo = gera_individuo(N)

        populacao.append(individuo)

    return populacao

def algoritmo_genetico(N): # N: tamanho do tabuleiro (NxN)
    # Parâmetros: uma população de 20 indivíduos com 50 gerações
    tam_pop = 20
    num_geracoes = 50

    # Gera população inicial
    Populacao = gera_populacao_inicial(N, tam_pop)
    # Executa N gerações
    for geracao in range(num_geracoes):
        for i in range(tam_pop / 2):

            # Seleciona dois candidatos
            p1 = selecao(Populacao)
            p2 = selecao(Populacao)
            crossover2(p1,p2)
            p2 = mutacao(p1)
            # Função fitness
            gera_tuplas_custos(Populacao)
    # ...
    # coloque seu código aqui
    pass

VT = np.array([4,8,2,7,3,7,5,4])
aux.converte_tabuleiro(VT)
aux.conta_ataques(VT)
Populacao = aux.gera_vizinhos(VT) # <=== TROCAR P GERAR SOLUÇÕES ALEATORIAS; CHAMAR N VEZES P GERAR A POPULAÇÃO
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