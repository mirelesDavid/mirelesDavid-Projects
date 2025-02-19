import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Definir los datos del problema
c = [8, 6, 7, 4, 3, 7, 5, 6]  # Costos por agente y posición

# Restricciones
A_eq = [[1, 1, 0, 0, 1, 1, 0, 0],  # Agente 1
        [0, 0, 1, 1, 0, 0, 1, 1]]  # Agente 2

b_eq = [2, 2]  # Capacidad de cada agente

# Resolver el problema
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, 1)] * 8, method='simplex')

# Extraer la solución
solution = result.x.round()

# Crear una gráfica enriquecida
fig, ax = plt.subplots(figsize=(10, 6))

# Información de los agentes y posiciones
agentes = ['Agente 1', 'Agente 2']
posiciones = ['Posición 1', 'Posición 2', 'Posición 3', 'Posición 4']

# Posicionar agentes y posiciones
x_agentes = np.zeros(len(agentes))  # Coordenada x fija para agentes
y_agentes = np.linspace(0, len(agentes) - 1, len(agentes))

x_posiciones = np.ones(len(posiciones)) * 3  # Coordenada x fija para posiciones
y_posiciones = np.linspace(0, len(posiciones) - 1, len(posiciones))

# Dibujar nodos para agentes
ax.scatter(x_agentes, y_agentes, s=600, color='lightblue', label='Agentes', edgecolors='black', zorder=3)
for i, (x, y) in enumerate(zip(x_agentes, y_agentes)):
    ax.text(x - 0.3, y, agentes[i], fontsize=10, ha='center', va='center', zorder=4)

# Dibujar nodos para posiciones
ax.scatter(x_posiciones, y_posiciones, s=600, color='lightgreen', label='Posiciones', edgecolors='black', zorder=3)
for i, (x, y) in enumerate(zip(x_posiciones, y_posiciones)):
    ax.text(x + 0.3, y, posiciones[i], fontsize=10, ha='center', va='center', zorder=4)

# Dibujar conexiones (aristas) según la solución óptima
costs = np.array(c).reshape(2, 4)
for i, agente in enumerate(agentes):
    for j, posicion in enumerate(posiciones):
        if solution[i * 4 + j] == 1:
            # Conexión óptima en rojo
            ax.plot([x_agentes[i], x_posiciones[j]], [y_agentes[i], y_posiciones[j]],
                    color='red', linewidth=2, zorder=2)
            # Etiqueta de costo
            mid_x = (x_agentes[i] + x_posiciones[j]) / 2
            mid_y = (y_agentes[i] + y_posiciones[j]) / 2
            ax.text(mid_x, mid_y, f'{costs[i, j]}', fontsize=9, color='darkred',
                    bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.6), zorder=5)
        else:
            # Conexión no seleccionada en gris claro
            ax.plot([x_agentes[i], x_posiciones[j]], [y_agentes[i], y_posiciones[j]],
                    color='gray', linestyle='--', alpha=0.5, zorder=1)

# Configurar la gráfica
ax.set_title("Asignación Óptima entre Agentes y Posiciones", fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper left', frameon=True, edgecolor='black')
ax.axis('off')

plt.tight_layout()
plt.show()

# Mostrar detalles de la solución
print(f"Costo total de la solución óptima: {result.fun:.2f}")
print("Asignaciones:")
for i, val in enumerate(solution):
    if val == 1:
        agent = agentes[i // 4]
        pos_idx = i % 4
        position = posiciones[pos_idx]
        print(f"{agent} -> {position} (Costo: {c[i]})")
