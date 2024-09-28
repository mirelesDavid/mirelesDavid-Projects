import sys

# Función para calcular el array de prefijos
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0  
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1] 
        if P[q] == T[i]:
            q += 1
        if q == m:
            print(f"Patrón ocurre con shift {i - m + 1}")
            q = pi[q - 1] 

def main():
    if len(sys.argv) != 2:
        print("Uso: python kmp.py archivo.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    try:
        with open(archivo, 'r') as file:
            contenido = file.read().strip()
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        sys.exit(1)

    patron = input("Introduce el patrón a buscar: ")

    kmp_matcher(contenido, patron)

if __name__ == "__main__":
    main()
