import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from matplotlib.animation import FuncAnimation

# Configuración inicial
np.random.seed(42)
num_agents = 5
num_tasks = 8
task_positions = np.random.rand(num_tasks, 2) * 100
agent_positions = np.random.rand(num_agents, 2) * 100
workload_threshold = 3  # Límite de tareas por agente

# Función objetivo: minimizar distancia total
c = []
for i in range(num_agents):
    for j in range(num_tasks):
        c.append(np.linalg.norm(agent_positions[i] - task_positions[j]))

# Restricciones de asignación de tareas
A_eq = []
b_eq = [1] * num_tasks  # Cada tarea debe ser asignada a un agente
for j in range(num_tasks):
    row = [0] * (num_agents * num_tasks)
    for i in range(num_agents):
        row[i * num_tasks + j] = 1
    A_eq.append(row)

# Restricciones de capacidad de agentes
A_ub = []
b_ub = [workload_threshold] * num_agents  # Límite de tareas por agente
for i in range(num_agents):
    row = [0] * (num_agents * num_tasks)
    for j in range(num_tasks):
        row[i * num_tasks + j] = 1
    A_ub.append(row)

# Resolver el problema
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=(0, 1), method='simplex')
assignments = result.x.reshape((num_agents, num_tasks))

# Identificar asignaciones
agent_tasks = []
for i in range(num_agents):
    agent_tasks.append([j for j in range(num_tasks) if assignments[i, j] > 0.5])

# Preparar la animación
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("Animación Simplificada: Asignación de Tareas")
ax.set_xlabel("Coordenada X")
ax.set_ylabel("Coordenada Y")

# Dibujar posiciones iniciales
tasks_scatter = ax.scatter(task_positions[:, 0], task_positions[:, 1], color='red', s=100, label='Tareas')
agents_scatter = ax.scatter(agent_positions[:, 0], agent_positions[:, 1], color='blue', s=100, label='Agentes')

# Líneas de conexión
lines = [ax.plot([], [], 'k-', alpha=0.5)[0] for _ in range(num_agents)]

# Función de inicialización
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Función de actualización
def update(frame):
    for i, tasks in enumerate(agent_tasks):
        if frame < len(tasks):
            task_idx = tasks[frame]
            agent_pos = agent_positions[i]
            task_pos = task_positions[task_idx]
            lines[i].set_data([agent_pos[0], task_pos[0]], [agent_pos[1], task_pos[1]])
    return lines

# Calcular el número de frames
total_frames = max(len(tasks) for tasks in agent_tasks)

# Crear la animación
ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=1000)

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Mostrar resultados en consola
print("\nAsignaciones finales:")
for i, tasks in enumerate(agent_tasks):
    print(f"Agente {i + 1}: Tareas asignadas -> {tasks}")
