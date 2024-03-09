import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import random
import numpy as np


# Leer el conjunto de datos
data = pd.read_csv('datos_ejemplo.csv')

# Normalizar los datos
data_normalized = (data - data.min()) / (data.max() - data.min())


def predict(x1, x2, m, b, c):
    prediction = m * x1 + c * x2 + b
    return 1 if prediction > 0.5 else 0


def loss_function(m, b, c, points):
    total_error = 0
    for i in range(len(points)):
        x1 = points.iloc[i].CO2
        x2 = points.iloc[i].GasesToxicos
        y = points.iloc[i].Resultado
        total_error += (y - (m * x1 + c * x2 + b)) ** 2
    return total_error / float(len(points))

def gradient_descent(m_now, b_now, c_now, points, L):
    m_gradient = 0
    b_gradient = 0
    c_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x1 = points.iloc[i].CO2
        x2 = points.iloc[i].GasesToxicos
        y = points.iloc[i].Resultado
        
        m_gradient += -(2/n) * x1 * (y - (m_now * x1 + c_now * x2 + b_now))
        c_gradient += -(2/n) * x2 * (y - (m_now * x1 + c_now * x2 + b_now))
        b_gradient += -(2/n) * (y - (m_now * x1 + c_now * x2 + b_now))
        
    # Manejo de desbordamiento
    m_now = np.clip(m_now, -1e9, 1e9)
    b_now = np.clip(b_now, -1e9, 1e9)
    c_now = np.clip(c_now, -1e9, 1e9)
    
    m = m_now - m_gradient * L
    c = c_now - c_gradient * L
    b = b_now - b_gradient * L
    
    return m, b, c

m = 0.01
b = 0.01
c = 0.01
L = 0.0001
epochs = 1000

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
        print(m, b, c)
    m, b, c = gradient_descent(m, b, c, data_normalized, L)

print(m, b, c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_normalized['CO2'], data_normalized['GasesToxicos'], data_normalized['Resultado'], c='black', marker='o')
ax.set_xlabel('CO2')
ax.set_ylabel('GasesToxicos')
ax.set_zlabel('Resultado')
X, Y = np.meshgrid(data_normalized['CO2'], data_normalized['GasesToxicos'])
Z = m * X + c * Y + b
ax.plot_surface(X, Y, Z, alpha=0.5, color='red')

co2_input = 750
gases_toxicos_input = 7

# Calcular la predicción
prediction = predict(co2_input, gases_toxicos_input, m, b, c)

# Mostrar la predicción
print("Input CO2: 750, Gases Toxicos 7%")
print(f"Prediccion: {prediction}")


# Mostrar el gráfico
plt.show()

