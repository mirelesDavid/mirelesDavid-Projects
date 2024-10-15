import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskalMST(W):
    n = len(W)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if W[i][j] != math.inf and W[i][j] >= 0:  # Evitar aristas negativas
                edges.append((W[i][j], i, j))
    edges.sort()

    uf = UnionFind(n)
    mst = []
    mst_weight = 0

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u + 1, v + 1, weight))
            mst_weight += weight

    return mst, mst_weight

def floydWarshall(matrix):
    numNodes = len(matrix)
    dp = [[matrix[i][j] for j in range(numNodes)] for i in range(numNodes)]
    pi = [[None if i == j or matrix[i][j] == math.inf else i + 1 for j in range(numNodes)] for i in range(numNodes)]

    for k in range(numNodes):
        for i in range(numNodes):
            for j in range(numNodes):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    pi[i][j] = pi[k][j]

    return dp, pi

def printNicely(matrix, title="Matrix"):
    print(f"{title}:")
    for row in matrix:
        print(" ".join(f"{value:7}" if value is not None and value != math.inf else "None" if value is None else "inf" for value in row))

def reconstructPath(source, target, pi):
    if pi[source - 1][target - 1] is None:
        return None

    path = [target]
    while source != target:
        target = pi[source - 1][target - 1]
        path.append(target)
    path.reverse()
    return path

if __name__ == "__main__":

    adjacencyMatrix = [
        [0, 3, 8, math.inf, -4],
        [math.inf, 0, math.inf, 1, 7],
        [math.inf, 4, 0, math.inf, math.inf],
        [2, math.inf, -5, 0, math.inf],
        [math.inf, math.inf, math.inf, 6, 0]
    ]

    distances, predecessors = floydWarshall(adjacencyMatrix)
    printNicely(distances, "Matriz de distancias mínimas (dp)")
    printNicely(predecessors, "Matriz de predecesores (π)")

    source = 1
    target = 3
    path = reconstructPath(source, target, predecessors)
    if path:
        print(f"Ruta más corta de {source} a {target}: {' -> '.join(map(str, path))}")
    else:
        print(f"No existe una ruta de {source} a {target}")

    mst, mst_weight = kruskalMST(adjacencyMatrix)

    print("\nÁrbol de expansión mínima (MST):")
    for u, v, weight in mst:
        print(f"Arista ({u}, {v}) con peso {weight}")
    print(f"\nPeso total del MST: {mst_weight}")
