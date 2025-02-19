#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <queue>
#include <climits>
#include <map>
#include <limits>
#include <numeric>
#include <fstream>

using namespace std;

const int INF = INT_MAX;

// Estructura para representar aristas
struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

// *1. Árbol de expansión mínima usando el algoritmo de Kruskal*
int find(int x, vector<int>& parent) {
    if (x != parent[x]) {
        parent[x] = find(parent[x], parent); // Compresión de caminos
    }
    return parent[x];
}

void unite(int x, int y, vector<int>& parent) {
    parent[find(x, parent)] = find(y, parent);
}

vector<Edge> kruskalMST(int N, const vector<vector<int>>& graph) {
    vector<Edge> edges, mst;
    vector<int> parent(N);
    iota(parent.begin(), parent.end(), 0);

    // Convertir matriz de adyacencia a lista de aristas
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (graph[i][j] != 0 && graph[i][j] != INF) {
                edges.push_back({i, j, graph[i][j]});
            }
        }
    }

    sort(edges.begin(), edges.end());

    for (const auto& edge : edges) {
        if (find(edge.u, parent) != find(edge.v, parent)) {
            mst.push_back(edge);
            unite(edge.u, edge.v, parent);
        }
    }
    return mst;
}

// *2. Problema del Viajero (TSP) usando DP + Bitmask*
pair<int, vector<int>> tsp(const vector<vector<int>>& graph) {
    int N = graph.size();
    vector<vector<int>> dp(1 << N, vector<int>(N, INF));
    vector<vector<int>> parent(1 << N, vector<int>(N, -1));

    dp[1][0] = 0; // Comienza en la ciudad 0

    for (int mask = 1; mask < (1 << N); ++mask) {
        for (int u = 0; u < N; ++u) {
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < N; ++v) {
                if (mask & (1 << v)) continue;
                int newMask = mask | (1 << v);
                int cost = dp[mask][u] + graph[u][v];
                if (cost < dp[newMask][v]) {
                    dp[newMask][v] = cost;
                    parent[newMask][v] = u;
                }
            }
        }
    }

    int minCost = INF, last = -1;
    for (int u = 1; u < N; ++u) {
        int cost = dp[(1 << N) - 1][u] + graph[u][0];
        if (cost < minCost) {
            minCost = cost;
            last = u;
        }
    }

    vector<int> route;
    for (int mask = (1 << N) - 1, u = last; u != -1; u = parent[mask][u]) {
        route.push_back(u);
        mask ^= (1 << u);
    }
    reverse(route.begin(), route.end());
    return {minCost, route};
}

// *3. Flujo máximo usando Edmonds-Karp*
int maxFlowEdmondsKarp(int N, vector<vector<int>>& capacity, int source, int sink) {
    vector<vector<int>> flow(N, vector<int>(N, 0));
    int maxFlow = 0;

    while (true) {
        vector<int> parent(N, -1);
        queue<pair<int, int>> q;
        q.push({source, INF});

        while (!q.empty() && parent[sink] == -1) {
            int u = q.front().first;
            int currFlow = q.front().second;
            q.pop();

            for (int v = 0; v < N; ++v) {
                if (parent[v] == -1 && capacity[u][v] - flow[u][v] > 0) {
                    parent[v] = u;
                    int newFlow = min(currFlow, capacity[u][v] - flow[u][v]);
                    if (v == sink) {
                        maxFlow += newFlow;
                        for (int x = v; x != source; x = parent[x]) {
                            int y = parent[x];
                            flow[y][x] += newFlow;
                            flow[x][y] -= newFlow;
                        }
                        goto nextIteration;
                    }
                    q.push({v, newFlow});
                }
            }
        }
        break;
    nextIteration:;
    }

    return maxFlow;
}

// *4. Distancia Euclidiana*
double euclideanDistance(pair<int, int> a, pair<int, int> b) {
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

void printDistances(const vector<pair<int, int>>& colonies, const vector<pair<int, int>>& centrals) {
    cout << "\nDistancias entre colonias y centrales:\n";
    for (int i = 0; i < colonies.size(); ++i) {
        cout << "Colonia " << char('A' + i) << ":\n";
        for (int j = 0; j < centrals.size(); ++j) {
            double distance = euclideanDistance(colonies[i], centrals[j]);
            cout << "  Central " << char('A' + j) << " Distancia: " << distance << "\n";
        }
    }
}

int main() {
    ifstream input("input.txt");
    if (!input) {
        cerr << "Error al abrir el archivo de entrada.\n";
        return 1;
    }

    int N;
    input >> N;

    vector<vector<int>> distances(N, vector<int>(N));
    vector<vector<int>> capacities(N, vector<int>(N));
    vector<pair<int, int>> coordinates(N);

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            input >> distances[i][j];

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            input >> capacities[i][j];

    for (int i = 0; i < N; ++i)
        input >> coordinates[i].first >> coordinates[i].second;

    // 1. Árbol de expansión mínima
    auto mst = kruskalMST(N, distances);
    cout << "Forma de cablear con fibra:\n";
    for (const auto& edge : mst) {
        cout << "(" << char('A' + edge.u) << "," << char('A' + edge.v) << ")\n";
    }

    // 2. Ruta del vendedor viajero (TSP)
    auto [minCost, route] = tsp(distances);
    cout << "\nRuta del vendedor viajero:\n";
    for (int city : route) {
        cout << char('A' + city) << " ";
    }
    cout << char('A' + route[0]) << "\n";

    // 3. Flujo máximo
    int source = 0, sink = N - 1;
    int maxFlow = maxFlowEdmondsKarp(N, capacities, source, sink);
    cout << "\nFlujo maximo de datos: " << maxFlow << "\n";

    // 4. Distancias entre colonias y centrales
    printDistances(coordinates, coordinates);

    return 0;
}