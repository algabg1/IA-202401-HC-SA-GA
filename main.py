import time, os
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
'''
inicio = time.time()
custo, vetor_melhor = (hillclimbing.hill_climbing_restart(vetor))
fim = time.time()
print("tempo de execução do Hill-Climbing:", fim - inicio)
'''