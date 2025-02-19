from ortools.linear_solver import pywraplp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración del problema
num_positions = 6  # Número de posiciones de monedas
num_teams = 2      # Número de equipos
max_assignments = 3  # Límite de asignaciones por equipo

# Valores de monedas y posiciones
values = [10, 15, 20, 25, 30, 35]
positions = np.random.rand(num_positions, 2) * 10  # Coordenadas aleatorias de monedas

# Crear el solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Variables de decisión: x[i][j] = 1 si el equipo i recoge en la posición j, 0 de lo contrario
x = [[solver.IntVar(0, 1, f'x[{i},{j}]') for j in range(num_positions)] for i in range(num_teams)]

# Restricción: Cada posición solo puede ser asignada a un equipo
for j in range(num_positions):
    solver.Add(sum(x[i][j] for i in range(num_teams)) <= 1)

# Restricción: Cada equipo puede recolectar en un máximo de posiciones
for i in range(num_teams):
    solver.Add(sum(x[i][j] for j in range(num_positions)) <= max_assignments)

# Función objetivo: Maximizar el valor recolectado
objective = solver.Objective()
for i in range(num_teams):
    for j in range(num_positions):
        objective.SetCoefficient(x[i][j], values[j])
objective.SetMaximization()

# Resolver el problema
status = solver.Solve()

# Procesar resultados
if status == pywraplp.Solver.OPTIMAL:
    team_assignments = [[int(x[i][j].solution_value()) for j in range(num_positions)] for i in range(num_teams)]
    team_values = [sum(team_assignments[i][j] * values[j] for j in range(num_positions)) for i in range(num_teams)]

    # Configuración de la animación
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Animación: Colaboración Óptima entre Equipos")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Colores de los equipos
    team_colors = ['blue', 'green']

    # Graficar posiciones de monedas
    coins = ax.scatter(positions[:, 0], positions[:, 1], c='gold', s=200, label="Monedas")
    labels = []
    for i, pos in enumerate(positions):
        label = ax.text(pos[0], pos[1], f"{values[i]}", fontsize=10, ha='center', va='center')
        labels.append(label)

    # Inicializar posiciones de los equipos (punto de origen)
    team_positions = np.zeros((num_teams, 2))
    team_dots = [ax.plot([], [], 'o', color=team_colors[i], markersize=10, label=f"Equipo {i + 1}")[0] for i in range(num_teams)]

    # Crear trayectorias para cada equipo
    team_paths = [[] for _ in range(num_teams)]
    for team in range(num_teams):
        for i, assigned in enumerate(team_assignments[team]):
            if assigned == 1:
                team_paths[team].append(positions[i])

    # Función de inicialización
    def init():
        for dot in team_dots:
            dot.set_data([], [])
        return team_dots

    # Función de actualización
    def update(frame):
        for team in range(num_teams):
            if frame < len(team_paths[team]):
                team_positions[team] = team_paths[team][frame]
                team_dots[team].set_data(team_positions[team][0], team_positions[team][1])
        return team_dots

    # Crear animación
    ani = animation.FuncAnimation(fig, update, frames=max(len(p) for p in team_paths), init_func=init, blit=True, interval=1000)

    plt.legend()
    plt.show()

    # Resultados en consola
    print("Asignaciones por equipo:", team_assignments)
    print("Valores recolectados por cada equipo:", team_values)
else:
    print("No se encontró una solución óptima.")
