#include <fstream>
#include <iostream>
#include <limits>
#include <chrono>
#include <stdexcept> // Para manejo de excepciones

using namespace std;
using namespace std::chrono;

void merge(int A[], int p, int q, int r) {
    int n1 = q - p + 1;
    int n2 = r - q;
    int L[n1 + 1], R[n2 + 1];
    for (int i = 0; i < n1; i++) {
        L[i] = A[p + i];
    }
    for (int i = 0; i < n2; i++) {
        R[i] = A[q + i + 1];
    }
    L[n1] = numeric_limits<int>::max();
    R[n2] = numeric_limits<int>::max();

    int i = 0, j = 0;
    for (int k = p; k <= r; k++) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i = i + 1;
        } else {
            A[k] = R[j];
            j = j + 1;
        }
    }
}

void merge_sort(int a[], int inicio, int fin) {
    int mitad;
    if (inicio < fin) {
        mitad = (inicio + fin) / 2;
        merge_sort(a, inicio, mitad); // Procesa el subarreglo izquierdo
        merge_sort(a, mitad + 1, fin); // Procesa el subarreglo derecho
        merge(a, inicio, mitad, fin); // Unir 
    }
}

void print_array(int a[], int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Uso: " << argv[0] << " <archivo de entrada>" << endl;
        return 1;
    }

    int n, i;
    string s;
    ifstream in(argv[1]);

    if (!in) {
        cerr << "Error al abrir el archivo " << argv[1] << endl;
        return 1;
    }

    try {
        getline(in, s);
        n = stoi(s);  // Convertir la primera línea a entero
        
        int *arreglo = new int[n];
        i = 0;

        while (getline(in, s)) {
            if (!s.empty()) {  // Ignorar líneas en blanco
                arreglo[i] = stoi(s);
                i++;
            }
        }

        if (i != n) {
            cerr << "Advertencia: la cantidad de números leídos no coincide con la cantidad especificada." << endl;
        }


        auto start = high_resolution_clock::now();
        merge_sort(arreglo, 0, n - 1);
        auto stop = high_resolution_clock::now();

        auto duration = duration_cast<nanoseconds>(stop - start);
        cout << "Tiempo de ejecucion: " << duration.count() << " nanoseconds" << endl;
        delete[] arreglo;

    } catch (const invalid_argument &e) {
        cerr << "Error: argumento inválido al convertir a entero. " << e.what() << endl;
        return 1;
    } catch (const out_of_range &e) {
        cerr << "Error: número fuera del rango. " << e.what() << endl;
        return 1;
    }

    return 0;
}
