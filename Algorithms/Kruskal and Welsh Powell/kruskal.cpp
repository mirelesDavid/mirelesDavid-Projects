#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <queue>
#include <set>
using namespace std;

struct GraphEdge {
    int sourceNode, destinationNode, edgeWeight;
    bool operator<(const GraphEdge& other) const {
        return edgeWeight < other.edgeWeight;
    }
};

class Graph {
    int totalNodes;
    vector<GraphEdge> edgeList;
    vector<vector<int>> adjacencyMatrix;
public:
    Graph(int totalNodes);
    void addGraphEdge(int sourceNode, int destinationNode, int edgeWeight);
    void loadAdjacencyMatrixFromFile(const string& fileName);
    void generateKruskalMST(const string& outputFileName);
    void applyWelshPowellAlgorithm(const string& outputFileName);
    void resetGraphData();
};

Graph::Graph(int totalNodes) : totalNodes(totalNodes) {
    adjacencyMatrix.resize(totalNodes, vector<int>(totalNodes, 0));
}

void Graph::resetGraphData() {
    edgeList.clear();
    adjacencyMatrix.assign(totalNodes, vector<int>(totalNodes, 0));
}

void Graph::addGraphEdge(int sourceNode, int destinationNode, int edgeWeight) {
    if (sourceNode != destinationNode && edgeWeight != 0) {
        edgeList.push_back({sourceNode, destinationNode, edgeWeight});
        adjacencyMatrix[sourceNode][destinationNode] = edgeWeight;
        adjacencyMatrix[destinationNode][sourceNode] = edgeWeight;
    }
}

void Graph::loadAdjacencyMatrixFromFile(const string& fileName) {
    ifstream inputFile(fileName);
    if (inputFile.is_open()) {
        resetGraphData();
        for (int i = 0; i < totalNodes; i++) {
            for (int j = 0; j < totalNodes; j++) {
                inputFile >> adjacencyMatrix[i][j];
                if (adjacencyMatrix[i][j] != 0 && i < j) {
                    addGraphEdge(i, j, adjacencyMatrix[i][j]);
                }
            }
        }
        inputFile.close();
    } else {
        cerr << "Error in: " << fileName << endl;
    }
}

int findParentSet(int node, vector<int>& parentNodes) {
    if (node != parentNodes[node])
        parentNodes[node] = findParentSet(parentNodes[node], parentNodes);
    return parentNodes[node];
}

void unionNodeSets(int node1, int node2, vector<int>& parentNodes, vector<int>& rank) {
    node1 = findParentSet(node1, parentNodes);
    node2 = findParentSet(node2, parentNodes);
    if (rank[node1] < rank[node2])
        parentNodes[node1] = node2;
    else if (rank[node1] > rank[node2])
        parentNodes[node2] = node1;
    else {
        parentNodes[node2] = node1;
        rank[node1]++;
    }
}

void Graph::generateKruskalMST(const string& outputFileName) {
    vector<GraphEdge> minimumSpanningTree;
    vector<int> parentNodes(totalNodes);
    vector<int> rank(totalNodes, 0);
    for (int i = 0; i < totalNodes; i++)
        parentNodes[i] = i;

    sort(edgeList.begin(), edgeList.end());

    for (const auto& edge : edgeList) {
        if (findParentSet(edge.sourceNode, parentNodes) != findParentSet(edge.destinationNode, parentNodes)) {
            minimumSpanningTree.push_back(edge);
            unionNodeSets(edge.sourceNode, edge.destinationNode, parentNodes, rank);
        }
    }

    ofstream outputFile(outputFileName, ios::trunc);
    if (outputFile.is_open()) {
        vector<vector<int>> mstMatrix(totalNodes, vector<int>(totalNodes, 0));
        for (const auto& edge : minimumSpanningTree) {
            mstMatrix[edge.sourceNode][edge.destinationNode] = edge.edgeWeight;
            mstMatrix[edge.destinationNode][edge.sourceNode] = edge.edgeWeight;
        }

        for (const auto& row : mstMatrix) {
            for (int value : row) {
                outputFile << value << " ";
            }
            outputFile << endl;
        }
        outputFile.close();
    }
}

void Graph::applyWelshPowellAlgorithm(const string& outputFileName) {
    vector<int> nodeColors(totalNodes, -1);
    vector<pair<int, int>> nodeDegrees(totalNodes);

    for (int i = 0; i < totalNodes; i++) {
        int degreeCount = 0;
        for (int j = 0; j < totalNodes; j++) {
            if (adjacencyMatrix[i][j] != 0) {
                degreeCount++;
            }
        }
        nodeDegrees[i] = make_pair(degreeCount, i);
    }

    sort(nodeDegrees.rbegin(), nodeDegrees.rend());

    int currentColor = 0;
    for (size_t i = 0; i < nodeDegrees.size(); i++) {
        int currentNode = nodeDegrees[i].second;
        if (nodeColors[currentNode] == -1) {
            nodeColors[currentNode] = currentColor;
            for (size_t j = i + 1; j < nodeDegrees.size(); j++) {
                int neighborNode = nodeDegrees[j].second;
                if (nodeColors[neighborNode] == -1) {
                    bool canBeColored = true;
                    for (int k = 0; k < totalNodes; k++) {
                        if (adjacencyMatrix[neighborNode][k] != 0 && nodeColors[k] == currentColor) {
                            canBeColored = false;
                            break;
                        }
                    }
                    if (canBeColored) {
                        nodeColors[neighborNode] = currentColor;
                    }
                }
            }
            currentColor++;
        }
    }

    ofstream outputFile(outputFileName, ios::trunc);
    if (outputFile.is_open()) {
        for (int i = 0; i < totalNodes; i++) {
            outputFile << "Vertex " << i << ": Color " << nodeColors[i] << endl;
        }
        outputFile.close();
    }
}

int getNodeCountFromFile(const string& fileName) {
    ifstream file(fileName);
    int lineCount = 0;
    string line;
    if (file.is_open()) {
        while (getline(file, line)) {
            lineCount++;
        }
        file.close();
    }
    return lineCount;
}

int main() {
    string adjacencyMatrixFileName = "matrizAdj.txt";
    int totalNodes = getNodeCountFromFile(adjacencyMatrixFileName);
    
    Graph graph(totalNodes);
    graph.loadAdjacencyMatrixFromFile(adjacencyMatrixFileName);
    
    cout << "Kruskal in mst.txt" << endl;
    graph.generateKruskalMST("mst.txt");
    
    cout << "WelshPowell in vertexColors.txt" << endl;
    graph.applyWelshPowellAlgorithm("vertexColors.txt");

    return 0;
}
