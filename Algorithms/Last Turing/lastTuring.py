import numpy as np
import random
import math


def calculate_distance(route, distance_matrix):
    """Calcula la distancia total para una ruta dada."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Regresar al inicio
    return total_distance


def generate_neighbor(route):
    """Genera un vecino de la ruta intercambiando dos ciudades."""
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def simulated_annealing(distance_matrix, initial_temperature, cooling_rate, max_iterations):
    """Algoritmo de Recocido Simulado para resolver el TSP."""
    num_cities = len(distance_matrix)
    current_solution = list(range(num_cities))
    random.shuffle(current_solution)
    current_cost = calculate_distance(current_solution, distance_matrix)

    best_solution = current_solution[:]
    best_cost = current_cost

    temperature = initial_temperature

    for iteration in range(max_iterations):
        new_solution = generate_neighbor(current_solution)
        new_cost = calculate_distance(new_solution, distance_matrix)

        # Criterio de aceptación
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

            # Actualizar mejor solución si mejora
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        # Enfriamiento
        temperature *= cooling_rate

        # Salida de estado actual
        print(f"Iteration {iteration + 1}: Best Cost = {best_cost}")

        # Detener si la temperatura es demasiado baja
        if temperature < 1e-8:
            break

    return best_solution, best_cost


# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de distancias (simétrica)
    distance_matrix = [
        [0, 29, 20, 21, 16],
        [29, 0, 15, 17, 28],
        [20, 15, 0, 35, 12],
        [21, 17, 35, 0, 25],
        [16, 28, 12, 25, 0],
    ]
    # Parámetros
    initial_temperature = 1000
    cooling_rate = 0.99
    max_iterations = 1000

    # Resolver el problema
    best_solution, best_cost = simulated_annealing(distance_matrix, initial_temperature, cooling_rate, max_iterations)

    print("\nBest Solution:", best_solution)
    print("Best Cost:", best_cost)
