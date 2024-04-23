import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import random
import numpy as np


data = []
data.append(["StudyTime", "TVTime", "Grade"])

for _ in range(250):
    study_time = round(random.uniform(0, 50), 2)
    tv_time = round(random.uniform(0, 10), 2)  
    grade = round(2 * study_time + 3 * tv_time + random.uniform(-10, 10), 2)
    grade = max(0, min(100, grade))
    data.append([study_time, tv_time, grade])

with open('datos_realisticos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Archivo CSV creado exitosamente.")


data = pd.read_csv('datos_realisticos.csv')


def loss_function(m, b, c, points):
    total_error = 0
    for i in range(len(points)):
        x1 = points.iloc[i].StudyTime
        x2 = points.iloc[i].TVTime
        y = points.iloc[i].Grade
        total_error += (y - (m * x1 + c * x2 + b)) ** 2
    return total_error / float(len(points))

def gradient_descent(m_now, b_now, c_now, points, L):
    m_gradient = 0
    b_gradient = 0
    c_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x1 = points.iloc[i].StudyTime
        x2 = points.iloc[i].TVTime
        y = points.iloc[i].Grade
        
        m_gradient += -(2/n) * x1 * (y - (m_now * x1 + c_now * x2 + b_now))
        c_gradient += -(2/n) * x2 * (y - (m_now * x1 + c_now * x2 + b_now))
        b_gradient += -(2/n) * (y - (m_now * x1 + c_now * x2 + b_now))
        
    m = m_now - m_gradient * L
    c = c_now - c_gradient * L
    b = b_now - b_gradient * L
    
    return m, b, c


m = 0
b = 0
c = 0
L = 0.0001
epochs = 10000


for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
        print(m, b, c)
    m, b, c = gradient_descent(m, b, c, data, L)

print(m, b, c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data['StudyTime'], data['TVTime'], data['Grade'], c='black', marker='o')
ax.set_xlabel('StudyTime')
ax.set_ylabel('TVTime')
ax.set_zlabel('Grade')
X, Y = np.meshgrid(data['StudyTime'], data['TVTime'])
Z = m * X + c * Y + b
ax.plot_surface(X, Y, Z, alpha=0.5, color='red')

# Mostrar el gráfico
plt.show()

studyTime = 50
tvTime = 10
grade = m * studyTime + c * tvTime + b
print("Tu resultado esperado es de:", grade)
