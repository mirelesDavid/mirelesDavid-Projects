#include <fstream>
#include <iostream>

using namespace std;

class Tuple{
  private:
    int min_val;
    int max_val;
  
  public:
    Tuple(int min_val, int max_val){
      this->min_val = min_val;
      this->max_val = max_val;
    }

    int get_min() const {
        return min_val;
    }

    int get_max() const {
        return max_val;
    }
};

Tuple maximin(int *A, int low, int high){
    if (low == high) {  
        return Tuple(A[low], A[low]);
    }
    
    if (high == low + 1) {  
        if (A[low] < A[high]) {
            return Tuple(A[low], A[high]);
        } else {
            return Tuple(A[high], A[low]);
        }
    }
    int mid = (low + high) / 2;
    Tuple left = maximin(A, low, mid);
    Tuple right = maximin(A, mid + 1, high);
    int min_val = min(left.get_min(), right.get_min());
    int max_val = max(left.get_max(), right.get_max());

    return Tuple(min_val, max_val);
}

int main(int argc, char *argv[]){
    int n, i;
    string s;
    ifstream in(argv[1]);
    getline(in, s);
    n = stoi(s);
    int *arreglo = new int[n];
    i = 0;
    while (getline(in, s))
    {
        arreglo[i] = stoi(s);
        cout << arreglo[i] << endl;
        i++;
    }

    Tuple result = maximin(arreglo, 0, n - 1);
    cout << "El mínimo del arreglo es: " << result.get_min() << " y el máximo es: " << result.get_max() << endl;

    delete[] arreglo;
    return 0;
}
