#include <fstream>
#include <iostream>
#include <limits>
#include <chrono>
#include <stdexcept> // Para manejo de excepciones

using namespace std;
using namespace std::chrono;

void quick_sort(int a[], int low, int high) {
    if (low < high) {
        int pivot = a[high]; // Elegir el último elemento como pivote
        int i = (low - 1); // Índice del elemento más pequeño

        for (int j = low; j < high; j++) {
            if (a[j] <= pivot) {
                i++;
                swap(a[i], a[j]);
            }
        }
        swap(a[i + 1], a[high]);
        int pi = i + 1;

        quick_sort(a, low, pi - 1);  // Ordenar los elementos a la izquierda del pivote
        quick_sort(a, pi + 1, high); // Ordenar los elementos a la derecha del pivote
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
        quick_sort(arreglo, 0, n - 1);
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
