import numpy as np
import random

def simulated_annealing(cities, initial_temperature, cooling_rate, iterations, nrep=50):

    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

    current_route = np.arange(num_cities)
    best_route = current_route.copy()

    current_distance = total_distance(current_route, distance_matrix)
    best_distance = current_distance

    temperature = initial_temperature

    #-----------------------------------------------
    iteration_list = []
    best_distances = []
    distance_list  = []
    accept_p_list  = []
    temperat_list  = []
    #-----------------------------------------------

    for iteration in range(iterations):

        # numero de vizinhos a serem gerados e testados para cada iteração
        for _ in range(nrep):

            new_route = generate_neighbor(current_route)
            new_distance = total_distance(new_route, distance_matrix)

            acceptance_prob = acceptance_probability(current_distance, new_distance, temperature)

            #print(acceptance_prob)

            if random.random() < acceptance_prob:
                current_route = new_route
                current_distance = new_distance

        temperature *= cooling_rate


        #-----------------------------------------------
        if new_distance < best_distance:
            best_route = new_route
            best_distance = new_distance

        iteration_list += [iteration]
        best_distances += [best_distance]
        distance_list  += [current_distance]
        accept_p_list  += [acceptance_prob]
        temperat_list  += [temperature]

        if iteration % 50 == 0:
            plot_axes_figure(cities, current_route, iteration_list,
                            distance_list, best_distances,
                            accept_p_list, temperat_list)
        #-----------------------------------------------

    # plt.show()

    return best_route, best_distance
