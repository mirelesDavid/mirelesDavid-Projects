import numpy as np
import matplotlib.pyplot as plt


def gradRosenbrock(x):
    gradient = np.zeros_like(x)
    gradient[:-1] = -400 * x[:-1] * (x[1:] - x[:-1]**2) - 2 * (1 - x[:-1])
    gradient[1:] += 200 * (x[1:] - x[:-1]**2)
    return gradient

def runGradientDescent(f, gradient, start, learningRate, maxIter=100, epsilon=1e-6, limits=None):
    pos = np.array(start)
    path = [pos.copy()]
    step = 0
    while np.linalg.norm(gradient(pos)) > epsilon and step < maxIter:
        gradVal = gradient(pos)
        nextPos = pos - learningRate * gradVal
        if limits is not None:
            nextPos = np.clip(nextPos, limits[0], limits[1])
        pos = nextPos
        path.append(pos.copy())
        step += 1
    return np.array(path)

def onePlusOneEvolutionStrategy(f, start, sigmaVal=None, maxGenerations=100, limits=None):
    if sigmaVal is None:
        sigmaVal = np.ones_like(start)
    pos = np.array(start)
    path = [pos.copy()]
    generation = 0
    while generation < maxGenerations:
        candidate = pos + sigmaVal * np.random.normal(0, 1, size=len(pos))
        if limits is not None:
            candidate = np.clip(candidate, limits[0], limits[1])
        if f(candidate) <= f(pos):
            pos = candidate
        path.append(pos.copy())
        generation += 1
    return np.array(path)

def showContourPlot(f, path, limits, title):
    zoomFactor = 1.5
    xLower, xUpper = limits[0] * zoomFactor, limits[1] * zoomFactor
    yLower, yUpper = limits[0] * zoomFactor, limits[1] * zoomFactor
    
    x = np.linspace(xLower, xUpper, 100)
    y = np.linspace(yLower, yUpper, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([f(np.array([xi, yi])) for xi, yi in zip(X.flatten(), Y.flatten())]).reshape(X.shape)
    
    plt.contour(X, Y, Z, levels=50, cmap='viridis')
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], 'ro-', markersize=3, label='Trajectory')
    plt.xlim(xLower, xUpper)
    plt.ylim(yLower, yUpper)
    plt.title(title)
    plt.legend()
    plt.show()
    
def rastriginFunc(x):
    a = 10
    return a * len(x) + np.sum(x**2 - a * np.cos(2 * np.pi * x))

def sphereFunc(x):
    return np.sum(x**2)

def rosenbrockFunc(v):
    return sum(100 * (v[1:] - v[:-1]**2)**2 + (1 - v[:-1])**2)

def gradSphere(x):
    return 2 * x

def gradRastrigin(x):
    a = 10
    return 2 * x + 2 * np.pi * a * np.sin(2 * np.pi * x)

testFunctions = [
    (sphereFunc, gradSphere, "Sphere", (-5.12, 5.12), 0.5),
    (rastriginFunc, gradRastrigin, "Rastrigin", (-5.12, 5.12), 0.001),
    (rosenbrockFunc, gradRosenbrock, "Rosenbrock", (-2.048, 2.048), 0.1)
]

sigmaValue = np.ones(2)

for func, gradFunc, funcName, bounds, alpha in testFunctions:
    initialPoint = np.random.uniform(bounds[0], bounds[1], size=2)
    pathGD = runGradientDescent(func, gradFunc, initialPoint, learningRate=alpha, limits=bounds)
    showContourPlot(func, pathGD, bounds, f"Gradient Descent on {funcName} with α={alpha}")

    initialPoint = np.random.uniform(bounds[0], bounds[1], size=2)
    pathES = onePlusOneEvolutionStrategy(func, initialPoint, sigmaVal=sigmaValue, maxGenerations=100, limits=bounds)
    showContourPlot(func, pathES, bounds, f"(1+1)-ES on {funcName}")
