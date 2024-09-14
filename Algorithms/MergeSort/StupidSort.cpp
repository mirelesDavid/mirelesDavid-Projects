#include <fstream>
#include <iostream>
#include <limits>
#include <chrono>
#include <stdexcept> // Para manejo de excepciones
#include <algorithm> // Para std::shuffle
#include <random>    // Para std::default_random_engine

using namespace std;
using namespace std::chrono;

// Función para verificar si el arreglo está ordenado
bool is_sorted(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) {
            return false;
        }
    }
    return true;
}

// Función de Stupid Sort (Bogosort)
void stupid_sort(int a[], int n) {
    random_device rd;
    mt19937 g(rd());
    while (!is_sorted(a, n)) {
        shuffle(a, a + n, g); // Mezcla los elementos aleatoriamente
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
        stupid_sort(arreglo, n);
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
