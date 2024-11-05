import random
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
        self.edges.append((u, v, weight))

    def generate_connected_graph(self):
        for i in range(1, self.V):
            weight = random.randint(1, 10)  
            self.add_edge(random.randint(0, i - 1), i, weight)

        for _ in range(self.V * 2):  
            u = random.randint(0, self.V - 1)
            v = random.randint(0, self.V - 1)
            if u != v and self.adj_matrix[u][v] == 0:
                weight = random.randint(1, 100)
                self.add_edge(u, v, weight)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.adj_matrix:
                f.write(' '.join(map(str, row)) + '\n')
                print(' '.join(map(str, row)))
        print(f'Guardado en {filename}')

def main():
    if len(sys.argv) != 2:
        print("Uso: python generador_grafo.py <numero_de_vertices>")
        sys.exit(1)

    try:
        num_vertices = int(sys.argv[1])
        if num_vertices < 1:
            raise ValueError
    except ValueError:
        print("Por favor, proporciona un número entero positivo.")
        sys.exit(1)

    graph = Graph(num_vertices)
    graph.generate_connected_graph()
    graph.save_to_file('matrizAdj.txt')

if __name__ == '__main__':
    main()

