import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coeficientes de la función objetivo (negativos porque queremos maximizar)
c = [-5, -4, -6]

# Matriz de restricciones
A = [
    [1, 1, 1],  # Tiempo total
    [2, 1, 3]   # Capacidad máxima
]

# Límites de las restricciones
b = [10, 12]

# Límites de las variables (no negativos)
x_bounds = (0, None)

# Resolver el problema
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds] * 3, method='simplex')

# Datos obtenidos
x1, x2, x3 = result.x

# Gráfica de resultados
labels = ['Posición 1', 'Posición 2', 'Posición 3']
values = [x1, x2, x3]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'orange', 'green'])
plt.title('Cantidad óptima de monedas recolectadas en cada posición')
plt.ylabel('Cantidad de monedas')
plt.xlabel('Posiciones')
plt.ylim(0, max(values) + 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar valor máximo
plt.text(1, max(values), f"Valor máximo: {-result.fun:.2f}", ha='center', fontsize=10, color='red')

plt.show()
