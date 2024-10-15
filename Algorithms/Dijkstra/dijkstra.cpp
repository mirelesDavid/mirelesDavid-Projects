#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<vector<int>> readAdjacencyMatrixFromFile(const string& fileName) {
    ifstream file(fileName);
    if (!file.is_open()) {
        exit(1);
    }

    vector<vector<int>> adjacencyMatrix;
    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        vector<int> row;
        int weight;
        while (ss >> weight) {
            row.push_back(weight);
        }
        adjacencyMatrix.push_back(row);
    }

    file.close();
    return adjacencyMatrix;
}

pair<vector<int>, vector<int>> dijkstra(const vector<vector<int>>& adjacencyMatrix, int sourceNode) {
    int numNodes = adjacencyMatrix.size();
    vector<int> distances(numNodes, INF);
    vector<int> prev(numNodes, -1);
    distances[sourceNode] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, sourceNode});

    while (!pq.empty()) {
        int currentDistance = pq.top().first;
        int currentNode = pq.top().second;
        pq.pop();

        if (currentDistance > distances[currentNode]) {
            continue;
        }

        for (int neighbor = 0; neighbor < numNodes; ++neighbor) {
            int weight = adjacencyMatrix[currentNode][neighbor];
            if (weight > 0) {
                int newDistance = currentDistance + weight;
                if (newDistance < distances[neighbor]) {
                    distances[neighbor] = newDistance;
                    prev[neighbor] = currentNode;
                    pq.push({newDistance, neighbor});
                }
            }
        }
    }
    return {distances, prev};
}

vector<vector<int>> buildShortestPathAdjacencyMatrix(const vector<vector<int>>& originalMatrix, const vector<int>& prev) {
    int numNodes = originalMatrix.size();
    vector<vector<int>> shortestPathMatrix(numNodes, vector<int>(numNodes, 0));

    for (int node = 0; node < numNodes; ++node) {
        if (prev[node] != -1) {
            int from = prev[node];
            int to = node;
            shortestPathMatrix[from][to] = originalMatrix[from][to];
            shortestPathMatrix[to][from] = originalMatrix[to][from];
        }
    }

    return shortestPathMatrix;
}

void writeAdjacencyMatrixToFile(const vector<vector<int>>& matrix, const string& outputFileName) {
    ofstream file(outputFileName);
    if (!file.is_open()) {
        exit(1);
    }

    for (const auto& row : matrix) {
        for (size_t idx = 0; idx < row.size(); ++idx) {
            file << row[idx] << (idx == row.size() - 1 ? "\n" : " ");
        }
    }

    file.close();
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        return 1;
    }

    string inputFileName = argv[1];
    int sourceNode = stoi(argv[2]);

    vector<vector<int>> adjacencyMatrix = readAdjacencyMatrixFromFile(inputFileName);

    pair<vector<int>, vector<int>> result = dijkstra(adjacencyMatrix, sourceNode);
    vector<int> distances = result.first;
    vector<int> prev = result.second;

    vector<vector<int>> shortestPathMatrix = buildShortestPathAdjacencyMatrix(adjacencyMatrix, prev);

    string outputFileName = "shortpath.txt";
    writeAdjacencyMatrixToFile(shortestPathMatrix, outputFileName);

    cout << "Shortest path adjacency matrix saved to " << outputFileName << endl;

    return 0;
}
