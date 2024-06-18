'''import time, os
import hillclimbing as HG, simulatedannealing as SA, geneticalgorithm as GA, plotagem as plot


vetor = [4,8,2,7,3,7,5,4]
algoritmo = 'simulated_annealing'
output_directory = "tabuleiros"
output_filename = f"{algoritmo}_8_rainhas.png"
custo, vetor_melhor = (SA.simulated_annealing(vetor))


if not os.path.exists(output_directory):
    os.makedirs(output_directory)

save_path = os.path.join(output_directory, output_filename)

plot.plota_tabuleiro(vetor_melhor, save_path)

inicio = time.time()
custo, vetor_melhor = (hillclimbing.hill_climbing_restart(vetor))
fim = time.time()
print("tempo de execução do Hill-Climbing:", fim - inicio)
'''

import random
import math
import numpy as np

import matplotlib.pyplot as plt
from IPython.display import clear_output

# Cria uma solucao inicial com as rainhas em um ordem aleatoria
def solucao_aleatoria():
    return random.sample(range(1,9), 8)

# Função que recebe um Vetor-Tabuleiro e retorna o 
# número de pares de rainhas se atacando mutuamente nas linhas.
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

    return ataques

# Função que recebe um Vetor-Tabuleiro e retorna o número de 
# pares de rainhas se atacando mutuamente nas linhas e diagonais.

# função-objetivo o número de pares de rainhas se atacando
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
                
                
# Seleciona melhor vizinho
def obtem_melhor_vizinho(tabuleiro, solucao_inicial):
    #solucao aleatoria que foi criada
    melhor_custo = conta_ataques(solucao_inicial) 
    melhor_vizinho = solucao_inicial

    for vizinho in gera_vizinhos(solucao_inicial):
        custo_atual = conta_ataques(vizinho)
        if custo_atual < melhor_custo:
            melhor_custo = custo_atual
            melhor_vizinho = vizinho

    return melhor_vizinho, melhor_custo

# Plota o gráfico de probabilidade aceitação

def plot_acceptance_prob(iteration_list, accept_p_list, ax):

    x = iteration_list
    y = accept_p_list

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Probabilidade')
    ax.set_title('Probabilidade de Aceitação')

    ax.set_ylim([0, 1.05])

    # Criar uma nova lista de cores com base nos valores de y
    xc, yc, colors = zip(*[(xi, yi, 'b') if yi==1.0 else (xi, yi, 'r') \
                           for xi, yi in enumerate(y)])

    ax.scatter(xc, yc, c=colors, s=2)
    
# Plota o gráfico de temperatura

def plot_temperature(iteration_list, temperat_list, ax):

    x = iteration_list
    y = temperat_list

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Temperatura')
    ax.set_title('Decaimento da Temperatura')

    ax.set_ylim([0, 1000])

    ax.plot(x,y)
    
# Atualiza os gráficos de custos

def plot_custos(iteration_list, lista_conflitos, lista_melhor_conflitos, ax):
    
    x = iteration_list
    y1 = lista_conflitos
    y2 = lista_melhor_conflitos
    
    # Personalização do gráfico
    color = 'tab:red'
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Qnt de Ataques (Custos)')
    ax.plot(x,y1, label='Atual', color=color)
    ax.tick_params(axis='y', labelcolor=color)
    
    ax.set_title('Quantidade de ataques possíveis por iteração')
    
    ax1 = ax.tick_params(axis='y', labelcolor=color)
    
    color = 'tab:blue'
    ax1.set_ylabel('Qnt de Ataques (Melhores Custos)')
    ax1.plot(x,y2, label='Melhor', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax.legend()
    
# Atualiza os gráficos

def plot_axes_figure_hc(iteration_list, lista_melhor_conflitos, lista_conflitos):

    x = iteration_list    
    y1 = lista_conflitos
    y2 = lista_melhor_conflitos

    clear_output(wait=True)

    #Plota tabuleiro
    
    fig, ax1 = plt.subplots()
    
    #plot_custos(x, y1, y2, ax1)
    
    # Personalização do gráfico
    color = 'tab:red'
    ax1.set_xlabel('Iterações')
    ax1.set_ylabel('Qnt de Ataques (Custos)', color=color)
    ax1.plot(x,y1, label='Atual', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    #ax1.set_title('Quantidade de ataques possíveis por iteração')
    
    ax2 = ax1.twinx()
    
    color = 'tab:blue'
    ax2.set_ylabel('Qnt de Ataques (Melhores Custos)')
    ax2.plot(x,y2, label='Melhor', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    #ax1.legend()

    # Ajusta o espaçamento entre os subgráficos
    fig.tight_layout()
    
    #plt.pause(0.001)
    
    plt.show()
    
# Plota o tabuleiro

def plota_tabuleiro(positions):
    fig, ax = plt.subplots()
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks(range(9))
    ax.set_yticks(range(9))
    ax.grid(True)
    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, fill=True, color='lightgrey'))
            else:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, fill=True, color='white'))
    
    for col, row in enumerate(positions):
        ax.text(col + 0.5, row - 0.5, '♛', fontsize=30, ha='center', va='center', color='black')
    
    plt.gca().invert_yaxis()
    plt.gca().xaxis.tick_top()

    plt.show()
    
# HILL-CLIMBING COM RESTART
def hill_climbing_restart(tabuleiro):
    
    #print("Tabuleiro recebido:", tabuleiro)
    lista_tabuleiro = []
    lista_iteracoes = []
    lista_melhor_conflitos = []
    lista_conflitos = []
    
    # Parâmetro: 20 restarts
    for iteracao in range(20):
        
        #print("Iteração", iteracao+1)
        
        # solucao inicial
        solucao_atual = solucao_aleatoria()
        
        #print("Solução gerada aleatoriamente:", solucao_atual)
        
        # melhor solucao ate o momento
        solucao_melhor, custo_melhor = obtem_melhor_vizinho(tabuleiro, solucao_atual)
        
        #print("Melhor solução até o momento:", solucao_melhor, "com custo", custo_melhor)
        
        while True:
            # tenta obter um candidato melhor
            candidato_atual, custo_atual = obtem_melhor_vizinho(tabuleiro, solucao_melhor)
            # print(custo_melhor, custo_atual)
            if custo_atual < custo_melhor:
                custo_melhor   = custo_atual
                solucao_melhor = candidato_atual
            else:
                break   # custo nao melhorou, entao sai do while
        
        lista_tabuleiro += [candidato_atual]
        lista_iteracoes += [iteracao]
        lista_melhor_conflitos += [custo_melhor]
        lista_conflitos  += [custo_atual]
        
        print(f"Iteração {iteracao}, melhor conflito: {custo_melhor}")
        plot_axes_figure_hc(lista_iteracoes, lista_melhor_conflitos, lista_conflitos)
        plota_tabuleiro(candidato_atual)
    
    return custo_melhor, solucao_melhor

vetorInicial = solucao_aleatoria()

print("Tabuleiro recebido:", vetorInicial, "com custo:", conta_ataques(vetorInicial))
plota_tabuleiro(vetorInicial)

custo, vetor_melhor = hill_climbing_restart(vetorInicial)

print("Melhor solução:", vetor_melhor, "com custo:", custo)
plota_tabuleiro(vetor_melhor)