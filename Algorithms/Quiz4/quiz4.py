import numpy as np

def euclideanDistance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def distanceMatrix(points):
    n = len(points)
    distMatrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclideanDistance(points[i], points[j])
            distMatrix[i][j] = dist
            distMatrix[j][i] = dist
    return distMatrix

def calculateU(A, alpha):
    distMatrix = distanceMatrix(A)
    U = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and distMatrix[i][j] > 0:
                U += 1 / (distMatrix[i][j] ** alpha)
    return U

def greedySubsetSelection(A, n, alpha):
    while len(A) > n:
        UA = calculateU(A, alpha)
        contributions = []
        
        for i in range(len(A)):
            AWithoutI = A[:i] + A[i+1:]
            UAWithoutI = calculateU(AWithoutI, alpha)
            contributions.append(UA - UAWithoutI)
        
        worstIndex = contributions.index(max(contributions))
        A.pop(worstIndex)
    
    return A


