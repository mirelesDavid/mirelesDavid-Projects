#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <limits>
#include <algorithm>

using namespace std;

struct Node {
    double x, y;
};

struct Compare {
    bool operator()(const pair<int, double>& a, const pair<int, double>& b) {
        return a.second > b.second;
    }
};

double euclideanDistance(const Node& a, const Node& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

unordered_map<int, Node> readNodes(ifstream& file) {
    unordered_map<int, Node> nodes;
    string line;

    while (getline(file, line)) {
        if (line.empty() || line[0] == '#') continue;
        int id;
        double x, y;
        stringstream ss(line);
        ss >> id >> x >> y;
        nodes[id] = {x, y};
    }
    return nodes;
}

unordered_map<int, vector<pair<int, double>>> readEdges(ifstream& file) {
    unordered_map<int, vector<pair<int, double>>> edges;
    string line;

    while (getline(file, line)) {
        if (line.empty() || line[0] == '#') continue;
        int u, v;
        double weight;
        stringstream ss(line);
        ss >> u >> v >> weight;
        edges[u].emplace_back(v, weight);
    }
    return edges;
}

pair<vector<int>, double> aStar(
    const unordered_map<int, Node>& nodes,
    const unordered_map<int, vector<pair<int, double>>>& edges,
    int start,
    int goal
) {
    unordered_map<int, double> gScore, fScore;
    unordered_map<int, int> cameFrom;

    for (const auto& node : nodes) {
        int id = node.first;  // Clave del mapa
        gScore[id] = numeric_limits<double>::infinity();
        fScore[id] = numeric_limits<double>::infinity();
    }
    gScore[start] = 0;
    fScore[start] = euclideanDistance(nodes.at(start), nodes.at(goal));

    priority_queue<pair<int, double>, vector<pair<int, double>>, Compare> openSet;
    openSet.emplace(start, fScore[start]);

    while (!openSet.empty()) {
        int current = openSet.top().first;
        openSet.pop();

        if (current == goal) {
            vector<int> path;
            while (cameFrom.find(current) != cameFrom.end()) {
                path.push_back(current);
                current = cameFrom[current];
            }
            path.push_back(start);
            reverse(path.begin(), path.end());
            return {path, gScore[goal]};
        }

        if (edges.find(current) != edges.end()) {
            for (const auto& edge : edges.at(current)) {
                int neighbor = edge.first;
                double weight = edge.second;

                double tentativeGScore = gScore[current] + weight;
                if (tentativeGScore < gScore[neighbor]) {
                    cameFrom[neighbor] = current;
                    gScore[neighbor] = tentativeGScore;
                    fScore[neighbor] = gScore[neighbor] + euclideanDistance(nodes.at(neighbor), nodes.at(goal));
                    openSet.emplace(neighbor, fScore[neighbor]);
                }
            }
        }
    }

    return {{}, numeric_limits<double>::infinity()};
}

void savePathToFile(const string& fileName, const vector<int>& path, const unordered_map<int, Node>& nodes) {
    ofstream file(fileName);
    if (!file.is_open()) {
        cerr << "Error: No se pudo abrir el archivo para guardar la ruta." << endl;
        return;
    }

    file << "# Path Nodes\n";
    for (int node : path) {
        file << node << " " << nodes.at(node).x << " " << nodes.at(node).y << endl;
    }

    file.close();
}

void readGraph(const string& fileName,
               unordered_map<int, Node>& nodes,
               unordered_map<int, vector<pair<int, double>>>& edges) {
    ifstream file(fileName);
    if (!file.is_open()) {
        cerr << "Error: No se pudo abrir el archivo: " << fileName << endl;
        exit(1);
    }

    string line;
    bool readingNodes = false;
    bool readingEdges = false;

    while (getline(file, line)) {
        if (line.empty()) continue;

        if (line == "# Nodes:") {
            readingNodes = true;
            readingEdges = false;
            continue;
        } else if (line == "# Edges:") {
            readingNodes = false;
            readingEdges = true;
            continue;
        }

        if (readingNodes) {
            int id;
            double x, y;
            stringstream ss(line);
            ss >> id >> x >> y;
            nodes[id] = {x, y};
        } else if (readingEdges) {
            int u, v;
            double weight;
            stringstream ss(line);
            ss >> u >> v >> weight;
            edges[u].emplace_back(v, weight);
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        cerr << "Uso: " << argv[0] << " <archivo_grafo> <nodo_inicio> <nodo_final>" << endl;
        return 1;
    }

    string fileName = argv[1];
    int startNode = stoi(argv[2]);
    int goalNode = stoi(argv[3]);

    unordered_map<int, Node> nodes;
    unordered_map<int, vector<pair<int, double>>> edges;

    // Leer el grafo desde el archivo
    readGraph(fileName, nodes, edges);

    // Ejecutar A*
    auto result = aStar(nodes, edges, startNode, goalNode);
    vector<int> path = result.first;
    double cost = result.second;

    if (!path.empty()) {
        cout << "Ruta más corta: ";
        for (size_t i = 0; i < path.size(); ++i) {
            cout << path[i] << (i == path.size() - 1 ? "\n" : " -> ");
        }
        cout << "Costo total: " << cost << endl;

        savePathToFile("path.txt", path, nodes);

        cout << "Ruta y grafo guardados para visualización." << endl;
    } else {
        cout << "No se encontró un camino entre los nodos proporcionados." << endl;
    }

    return 0;
}
