import time
import hillclimbing, simulatedannealing, geneticalgorithm


vetor = [4,8,2,7,3,7,5,4]
inicio = time.time()
custo, vetor_melhor = (hillclimbing.hill_climbing_restart(vetor))
fim = time.time()
print("tempo de execução do Hill-Climbing:", fim - inicio)