import sys
import matplotlib.pyplot as plt
import networkx as nx

def readAdjacencyMatrix(fileName):
    with open(fileName, 'r') as f:
        matrix = []
        for line in f:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def createGraphFromAdjacencyMatrix(matrix):
    graph = nx.Graph()
    numNodes = len(matrix)

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            if matrix[i][j] > 0:
                graph.add_edge(i, j, weight=matrix[i][j])
    
    return graph

def plotGraph(graph, title, fileName):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=10)
    plt.title(title)
    plt.savefig(fileName)
    plt.show()

def plotGraphsFromFiles(originalMatrixFile, shortestPathMatrixFile, outputImageName):
    originalMatrix = readAdjacencyMatrix(originalMatrixFile)
    shortestPathMatrix = readAdjacencyMatrix(shortestPathMatrixFile)

    originalGraph = createGraphFromAdjacencyMatrix(originalMatrix)
    shortestPathGraph = createGraphFromAdjacencyMatrix(shortestPathMatrix)

    plotGraph(originalGraph, "Original Graph", f"{outputImageName}_original.png")
    plotGraph(shortestPathGraph, "Shortest Path Subgraph", f"{outputImageName}_shortest_paths.png")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    originalMatrixFile = sys.argv[1]
    shortestPathMatrixFile = sys.argv[2]
    outputImageName = sys.argv[3]

    plotGraphsFromFiles(originalMatrixFile, shortestPathMatrixFile, outputImageName)
