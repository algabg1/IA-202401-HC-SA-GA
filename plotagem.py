# Geração de gráficos
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import clear_output

# Plota tabuleiro
def plota_tabuleiro(vetor):
    tabuleiro = np.zeros((8, 8))
    rainhas = vetor  # Cada valor representa a linha (1 a 8)

    for coluna, linha in enumerate(rainhas):
        tabuleiro[linha-1, coluna] = 1

    plt.imshow(tabuleiro, cmap='gray')
    plt.title('Posições das Rainhas')
    plt.xticks(range(8), range(1, 9))
    plt.yticks(range(8), range(1, 9))
    plt.grid(color='black', linestyle='-', linewidth=1)
    plt.show()

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

def plot_temperature(iteration_list, temperat_list, ax):

    x = iteration_list
    y = temperat_list

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Temperatura')
    ax.set_title('Decaimento da Temperatura')

    ax.set_ylim([0, 1000])

    ax.plot(x,y)

#----------------------------------------------------------------

def plot_axes_figure(iteration_list, accept_p_list, temperat_list):

    x = iteration_list
    y3 = accept_p_list
    y4 = temperat_list

    clear_output(wait=True)

    fig, ((ax3, ax4)) = plt.subplots(2, 2, figsize=(12,8))

    plot_acceptance_prob(x, y3, ax3)
    plot_temperature    (x, y4, ax4)

    # Ajusta o espaçamento entre os subgráficos
    fig.tight_layout()

    plt.pause(0.001)

#-----------------------------------------------------    