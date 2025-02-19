import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

# Valores de las monedas en las posiciones
values = [
    [10, 15, 20, 25],  # Valores para Agente 1
    [30, 10, 20, 15]   # Valores para Agente 2
]

# Tiempo requerido para cada posición por cada agente
times = [
    [2, 3, 4, 5],  # Tiempos para Agente 1
    [3, 2, 5, 4]   # Tiempos para Agente 2
]

# Restricciones generales
time_limit = [8, 10]  # Tiempo máximo para Agentes 1 y 2
position_limit = 1  # Cada posición puede ser cubierta por solo un agente

# Convertir a formato de programación lineal
c = [-v for row in values for v in row]  # Función objetivo (negativos para maximizar)
A_eq = []
b_eq = [1] * len(values[0])  # Cada posición debe ser cubierta una vez

# Crear restricciones de cobertura única por posición
for j in range(len(values[0])):
    row = [0] * (len(values) * len(values[0]))
    for i in range(len(values)):
        row[i * len(values[0]) + j] = 1
    A_eq.append(row)

# Restricciones de tiempo por agente
A_ub = []
b_ub = time_limit
for i in range(len(values)):
    row = [0] * (len(values) * len(values[0]))
    for j in range(len(values[0])):
        row[i * len(values[0]) + j] = times[i][j]
    A_ub.append(row)

# Límites de las variables
x_bounds = (0, 1)

# Resolver el problema
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds] * len(c), method='simplex')

# Procesar resultados
assignments = result.x.reshape(len(values), len(values[0])).round()
total_value = -result.fun

# Crear visualizaciones enriquecidas
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Representación espacial de posiciones y agentes
positions = np.array([[1, 1], [2, 3], [4, 5], [6, 2]])  # Coordenadas de las posiciones
agent_colors = ['blue', 'green']
for i, agent in enumerate(assignments):
    selected_positions = positions[agent == 1]
    axs[0].scatter(selected_positions[:, 0], selected_positions[:, 1], s=200, color=agent_colors[i], label=f'Agente {i+1}')
    for j, pos in enumerate(selected_positions):
        axs[0].text(pos[0], pos[1], f'P{j+1}', fontsize=10, ha='center', va='center')

axs[0].scatter(positions[:, 0], positions[:, 1], s=50, color='red', label='Posiciones')
axs[0].set_title('Asignaciones Espaciales de Agentes', fontsize=12, fontweight='bold')
axs[0].set_xlabel('Coordenada X')
axs[0].set_ylabel('Coordenada Y')
axs[0].legend()

# Gráfico 2: Comparación de valores y tiempos por posición
bar_width = 0.35
index = np.arange(len(values[0]))

for i, agent in enumerate(assignments):
    axs[1].bar(index + (i - 0.5) * bar_width, [values[i][j] for j in range(len(values[0]))], bar_width, 
               label=f'Agente {i+1} (Valor)', alpha=0.7, color=agent_colors[i])
    axs[1].bar(index + (i - 0.5) * bar_width, [times[i][j] for j in range(len(values[0]))], bar_width, 
               bottom=[values[i][j] for j in range(len(values[0]))], alpha=0.5, color='orange', label=f'Agente {i+1} (Tiempo)')

axs[1].set_title('Comparación de Valores y Tiempos por Posición', fontsize=12, fontweight='bold')
axs[1].set_xlabel('Posiciones')
axs[1].set_ylabel('Valor y Tiempo')
axs[1].set_xticks(index)
axs[1].set_xticklabels([f'P{i+1}' for i in range(len(values[0]))])
axs[1].legend()

# Resumen de resultados
plt.figtext(0.5, 0.02, f'Valor Total Maximizado: {total_value}', ha='center', fontsize=12, 
            bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

plt.tight_layout()
plt.show()

# Mostrar resultados detallados
print("\nAsignaciones por agente:")
for i, agent in enumerate(assignments):
    assigned_positions = [j+1 for j in range(len(agent)) if agent[j] == 1]
    print(f"Agente {i+1}: Posiciones {assigned_positions}")
print(f"\nValor total maximizado: {total_value}")
