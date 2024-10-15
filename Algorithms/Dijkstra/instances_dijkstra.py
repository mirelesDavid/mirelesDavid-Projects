import random
import sys

def generar_grafo(num_nodos, num_aristas, peso_maximo=10):
    grafo = {i: [] for i in range(num_nodos)}
    aristas_creadas = set()

    while len(aristas_creadas) < num_aristas:
        nodo1 = random.randint(0, num_nodos - 1)
        nodo2 = random.randint(0, num_nodos - 1)

        if nodo1 != nodo2 and (nodo1, nodo2) not in aristas_creadas and (nodo2, nodo1) not in aristas_creadas:
            peso = random.randint(1, peso_maximo)
            grafo[nodo1].append((nodo2, peso))
            grafo[nodo2].append((nodo1, peso))
            aristas_creadas.add((nodo1, nodo2))

    return grafo

def escribir_matriz_adyacencia(grafo, archivo_nombre):
    num_nodos = len(grafo)
    matriz = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)]
    
    for nodo, conexiones in grafo.items():
        for vecino, peso in conexiones:
            matriz[nodo][vecino] = peso
            matriz[vecino][nodo] = peso  

    with open(archivo_nombre, 'w') as archivo:
        for fila in matriz:
            archivo.write(" ".join(map(str, fila)) + "\n")

if __name__ == "__main__":
    num_nodos = int(sys.argv[1])
    num_aristas = int(sys.argv[2])
    archivo_nombre = sys.argv[3]

    grafo = generar_grafo(num_nodos, num_aristas)
    escribir_matriz_adyacencia(grafo, archivo_nombre)
