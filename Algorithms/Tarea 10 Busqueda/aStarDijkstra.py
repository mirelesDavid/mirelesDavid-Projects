import sys
import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def generateTxtReport(outputFileName, aStarPath, aStarCost, dijkstraPath, dijkstraCost):
    with open(outputFileName, 'w') as file:
        file.write("Shortest Path Comparison: A* vs Dijkstra\n")
        file.write("=" * 40 + "\n\n")
        file.write("A* Algorithm Results:\n")
        file.write(f"Path: {aStarPath}\n")
        file.write(f"Cost: {aStarCost:.2f}\n\n")
        file.write("Dijkstra Algorithm Results:\n")
        file.write(f"Path: {dijkstraPath}\n")
        file.write(f"Cost: {dijkstraCost:.2f}\n\n")
        file.write("=" * 40 + "\n")
        file.write("Report generated automatically by the program.\n")

def loadGraphFromFile(graphFileName):
    graph = nx.DiGraph()
    with open(graphFileName, 'r') as file:
        content = file.read()
    nodesSection, edgesSection = content.split("\n\n")
    for line in nodesSection.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        nodeId, posX, posY = map(float, line.split())
        graph.add_node(int(nodeId), pos=(posX, posY))
    for line in edgesSection.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        sourceNode, targetNode, edgeWeight = map(float, line.split())
        graph.add_edge(int(sourceNode), int(targetNode), weight=edgeWeight)
    return graph

def calculateHeuristic(startNode, goalNode, nodePositions):
    xStart, yStart = nodePositions[startNode]
    xGoal, yGoal = nodePositions[goalNode]
    return math.sqrt((xGoal - xStart) ** 2 + (yGoal - yStart) ** 2)

def aStarAlgorithm(graph, startNode, goalNode):
    nodePositions = nx.get_node_attributes(graph, 'pos')
    openSet = [(0, startNode)]
    cameFrom = {}
    gScores = {node: float('inf') for node in graph.nodes}
    gScores[startNode] = 0
    fScores = {node: float('inf') for node in graph.nodes}
    fScores[startNode] = calculateHeuristic(startNode, goalNode, nodePositions)

    while openSet:
        _, currentNode = heapq.heappop(openSet)
        if currentNode == goalNode:
            path = []
            while currentNode in cameFrom:
                path.append(currentNode)
                currentNode = cameFrom[currentNode]
            path.append(startNode)
            path.reverse()
            return path, gScores[goalNode]

        for neighbor in graph.neighbors(currentNode):
            tentativeGScore = gScores[currentNode] + graph[currentNode][neighbor]['weight']
            if tentativeGScore < gScores[neighbor]:
                cameFrom[neighbor] = currentNode
                gScores[neighbor] = tentativeGScore
                fScores[neighbor] = tentativeGScore + calculateHeuristic(neighbor, goalNode, nodePositions)
                heapq.heappush(openSet, (fScores[neighbor], neighbor))

    return None, float('inf')

def dijkstraAlgorithm(graph, startNode, goalNode):
    visitedNodes = set()
    minHeap = [(0, startNode)]
    cameFrom = {}
    distances = {node: float('inf') for node in graph.nodes}
    distances[startNode] = 0

    while minHeap:
        currentDistance, currentNode = heapq.heappop(minHeap)
        if currentNode in visitedNodes:
            continue
        visitedNodes.add(currentNode)

        if currentNode == goalNode:
            path = []
            while currentNode in cameFrom:
                path.append(currentNode)
                currentNode = cameFrom[currentNode]
            path.append(startNode)
            path.reverse()
            return path, distances[goalNode]

        for neighbor in graph.neighbors(currentNode):
            edgeWeight = graph[currentNode][neighbor]['weight']
            newDistance = currentDistance + edgeWeight
            if newDistance < distances[neighbor]:
                distances[neighbor] = newDistance
                cameFrom[neighbor] = currentNode
                heapq.heappush(minHeap, (newDistance, neighbor))

    return None, float('inf')

def plotGraphPath(graph, shortestPath, graphTitle):
    nodePositions = nx.get_node_attributes(graph, 'pos')
    edgeWeights = {(source, target): f"{data['weight']:.2f}" for source, target, data in graph.edges(data=True)}
    
    plt.figure(figsize=(12, 8))
    nx.draw(graph, nodePositions, with_labels=True, node_size=500, node_color='lightblue', arrows=True)
    nx.draw_networkx_edge_labels(graph, nodePositions, edge_labels=edgeWeights)
    if shortestPath:
        edgesInPath = [(shortestPath[i], shortestPath[i+1]) for i in range(len(shortestPath) - 1)]
        nx.draw_networkx_edges(graph, nodePositions, edgelist=edgesInPath, edge_color='red', width=2)
    plt.title(graphTitle, fontsize=16)
    plt.show()

def main():
    if len(sys.argv) != 4:
        print("Usage: python aStarDijkstra.py <graph_file> <start_node> <goal_node>")
        return
    
    graphFileName = sys.argv[1]
    startNode = int(sys.argv[2])
    goalNode = int(sys.argv[3])

    graph = loadGraphFromFile(graphFileName)
    aStarPath, aStarCost = aStarAlgorithm(graph, startNode, goalNode)
    dijkstraPath, dijkstraCost = dijkstraAlgorithm(graph, startNode, goalNode)

    print("A* Path:", aStarPath, "Cost:", aStarCost)
    print("Dijkstra Path:", dijkstraPath, "Cost:", dijkstraCost)

    plotGraphPath(graph, aStarPath, f"A* Path (Cost: {aStarCost:.2f})")
    plotGraphPath(graph, dijkstraPath, f"Dijkstra Path (Cost: {dijkstraCost:.2f})")

    txtFileName = "report.txt"
    generateTxtReport(txtFileName, aStarPath, aStarCost, dijkstraPath, dijkstraCost)

if __name__ == "__main__":
    main()
