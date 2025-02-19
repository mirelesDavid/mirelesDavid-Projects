import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

# Valores de monedas y tiempos en cada posición (no aleatorios)
values = [10, 15, 20, 25, 30]  # Valores de las monedas en las posiciones
times = [2, 3, 4, 5, 6]       # Tiempo requerido para recolectar monedas en cada posición
T_max = 10  # Tiempo máximo disponible

# Coeficientes de la función objetivo (negativos para maximizar)
c = [-v for v in values]

# Restricciones de tiempo
A = [times]  # Restricción de tiempo total
b = [T_max]  # Límite de tiempo disponible

# Límites de las variables
x_bounds = (0, 1)

# Resolver el problema
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds] * len(values), method='simplex')

# Procesar resultados
optimal_points = result.x.round()  # Variables de decisión (0 o 1)
total_value = -result.fun  # Valor total máximo recolectado
time_used = sum(np.array(times) * optimal_points)  # Tiempo utilizado

# Crear visualización enriquecida
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Distribución espacial de puntos seleccionados y no seleccionados
positions = np.linspace(0, 10, len(values))  # Coordenadas espaciales simples
selected_points = positions[optimal_points == 1]
unselected_points = positions[optimal_points == 0]

# Dibujar puntos
axs[0].scatter(selected_points, [1] * len(selected_points), color='green', s=100, label='Seleccionado', zorder=3)
axs[0].scatter(unselected_points, [1] * len(unselected_points), color='red', s=100, label='No Seleccionado', zorder=3)

# Etiquetas
for i, pos in enumerate(positions):
    axs[0].annotate(f'P{i+1}\nVal: {values[i]}\nT: {times[i]}', (pos, 1), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

axs[0].set_title('Distribución de Puntos Seleccionados y No Seleccionados', fontsize=12, fontweight='bold')
axs[0].set_yticks([])
axs[0].grid(axis='x', linestyle='--', alpha=0.5)
axs[0].legend(fontsize=10)
axs[0].set_xlabel("Posición en el Espacio")
axs[0].set_xlim(-1, 11)

# Gráfico 2: Comparación de valores y tiempos
bar_width = 0.4
index = np.arange(len(values))

axs[1].bar(index - bar_width/2, values, bar_width, color='blue', alpha=0.7, label='Valor')
axs[1].bar(index + bar_width/2, times, bar_width, color='orange', alpha=0.7, label='Tiempo')
axs[1].set_xticks(index)
axs[1].set_xticklabels([f'P{i+1}' for i in range(len(values))], fontsize=10)
axs[1].set_title('Comparación de Valores y Tiempos', fontsize=12, fontweight='bold')
axs[1].set_xlabel("Puntos")
axs[1].set_ylabel("Valor / Tiempo")
axs[1].legend(fontsize=10)

# Marcar puntos seleccionados con triángulos verdes
for i in range(len(values)):
    if optimal_points[i] == 1:
        axs[1].plot(i - bar_width/2, values[i], 'g^', markersize=10)
        axs[1].plot(i + bar_width/2, times[i], 'g^', markersize=10)

# Texto resumen de resultados
plt.figtext(0.5, 0.02,
            f'Valor Total Recolectado: {total_value} | Tiempo Utilizado: {time_used} de {T_max} disponible',
            ha='center', fontsize=12, bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

plt.tight_layout()
plt.show()

# Imprimir resumen detallado
print("\nResumen detallado:")
print("------------------")
print(f"Tiempo total disponible: {T_max}")
print(f"Tiempo utilizado: {time_used}")
print(f"Valor total recolectado: {total_value}")
print("\nDesglose por punto:")
for i in range(len(values)):
    status = "Seleccionado" if optimal_points[i] == 1 else "No seleccionado"
    print(f"Punto {i+1}: Valor={values[i]}, Tiempo={times[i]}, {status}")
