import numpy as np
import matplotlib.pyplot as plt

# Funciones objetivo
def esfera(v):
    return np.sum(v**2)

def rastrigin_func(v):
    A = 10
    return A * len(v) + np.sum(v**2 - A * np.cos(2 * np.pi * v))

def rosenbrock_func(v):
    return sum(100 * (v[1:] - v[:-1]**2)**2 + (1 - v[:-1])**2)

# Algoritmo (1+1)-ES modificado
def evolutionary_strategy(f, start, step=None, max_gen=100, lims=None):
    if step is None:
        step = np.ones_like(start)  # Vector de pasos iniciales en 1
    
    current = start
    path = [current]
    generation = 0
    
    while generation < max_gen:
        # Generar un candidato aleatorio
        candidate = current + step * np.random.normal(0, 1, size=len(current))
        
        # Aplicar límites
        if lims is not None:
            candidate = np.clip(candidate, lims[0], lims[1])

        # Selección
        if f(candidate) <= f(current):
            current = candidate
        
        path.append(current)
        generation += 1
    
    return np.array(path)

# Graficar resultados
def plot_trajectory(f, path, lims, title):
    x_range = np.linspace(lims[0], lims[1], 100)
    y_range = np.linspace(lims[0], lims[1], 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = np.array([f(np.array([xi, yi])) for xi, yi in zip(X.flatten(), Y.flatten())]).reshape(X.shape)

    plt.contour(X, Y, Z, levels=50, cmap='plasma')
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], 'bo-', markersize=3, label='Evolución')
    plt.title(title)
    plt.legend()
    plt.show()

# Ejecutar pruebas en funciones específicas con límites
test_cases = [
    (esfera, "Esfera", (-5.12, 5.12)),
    (rastrigin_func, "Rastrigin", (-5.12, 5.12)),
    (rosenbrock_func, "Rosenbrock", (-2.048, 2.048))
]

for func, func_name, limits in test_cases:
    initial_point = np.random.uniform(limits[0], limits[1], size=2)  # Punto de partida
    trace = evolutionary_strategy(func, initial_point, step=np.ones(2), max_gen=100, lims=limits)
    plot_trajectory(func, trace, limits, f"Estrategia Evolutiva en {func_name}")
