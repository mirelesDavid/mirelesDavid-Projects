#include <fstream>
#include <iostream>
#include <limits>

using namespace std;

class Result {
private:
    int low;
    int high;
    int sum;

public:
    Result(int low, int high, int sum) {
        this->low = low;
        this->high = high;
        this->sum = sum;
    }

    int get_low(){
        return low;
    }

    int get_high(){
        return high;
    }

    int get_sum(){
        return sum;
    }

};

Result find_max_crossing_subarray(int *A, int low, int mid, int high) {
    int leftSum = numeric_limits<int>::min();
    int sum = 0;
    int maxLeft = mid;

    for (int i = mid; i >= low; i--) {
        sum += A[i];
        if (sum > leftSum) {
            leftSum = sum;
            maxLeft = i;
        }
    }
    int rightSum = numeric_limits<int>::min();
    sum = 0;
    int maxRight = mid + 1;

    for (int i = mid + 1; i <= high; i++) {
        sum += A[i];
        if (sum > rightSum) {
            rightSum = sum;
            maxRight = i;
        }
    }
    return Result(maxLeft, maxRight, leftSum + rightSum);
}

Result find_maximum_subarray(int *A, int low, int high) {
    if (low == high) {
        return Result(low, high, A[low]);
    } else {
        int mid = (low + high) / 2;
        Result leftSide = find_maximum_subarray(A, low, mid);
        Result rightSide = find_maximum_subarray(A, mid + 1, high);
        Result crossed = find_max_crossing_subarray(A, low, mid, high);

        if (leftSide.get_sum() >= rightSide.get_sum() && leftSide.get_sum() >= crossed.get_sum()) {
            return leftSide;
        } else if (rightSide.get_sum() >= leftSide.get_sum() && rightSide.get_sum() >= crossed.get_sum()) {
            return rightSide;
        } else {
            return crossed;
        }
    }
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

    Result result = find_maximum_subarray(arreglo, 0, n - 1);
    cout << "La suma del máximo subarray es: " << result.get_sum() << endl;

    delete[] arreglo;
    return 0;
}
