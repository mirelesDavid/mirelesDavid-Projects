#include <iostream>
#include <algorithm>
#include <iterator>
#include <cstdlib>
#include <climits> 

using namespace std;

int memoized_cut_rod_aux(int *p, int n, int *r){
    if (r[n] >= 0){
        return r[n];
    }
    int q;
    if (n == 0)
        q = 0;
    else {
        q = INT_MIN;
        for (int i = 1; i <= n; i++) {
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r));
        }
    }
    r[n] = q;
    return q;
}

int memoized_cut_rod(int *p, int n){
    int *r = new int[n + 1];
    for (int i = 0; i <= n; i++) {
        r[i] = INT_MIN;
    }
    int result = memoized_cut_rod_aux(p, n, r);
    delete[] r;
    return result;
}

int bottom_up_cut_rod(int *p, int n) {
    int *r = new int[n + 1];
    r[0] = 0;
    int q;

    for (int j = 1; j <= n; j++) {
        q = INT_MIN;
        for (int i = 1; i <= j; i++) {
            q = max(q, p[i - 1] + r[j - i]);
        }
        r[j] = q;
    }

    int result = r[n];
    delete[] r;
    return result;
}
class Resultado{
    private:
        int *r;
        int *s;
    public:
    Resultado(int n){
        r = new int[n + 1];
        s = new int[n];
    }

    void set_r_at(int pos, int value){
        r[pos] = value;
    }

    void set_s_at(int pos, int value){
        s[pos] = value;
    }

    int get_r_at(int pos){
        return r[pos];
    }

    int get_s_at(int pos){
        return s[pos];
    }
};

Resultado extended_bottom_up_cut_rod(int *p, int n){
    Resultado res(n);
    res.set_r_at(0, 0);
    int q;
    for(int j = 1; j <= n; j++){
        q = -1;
        for(int i = 1; i <= j; i++){
            if( q < p[i - 1] + res.get_r_at(j - i)){
                q = p[i - 1] + res.get_r_at(j - i);
                res.set_s_at(j - 1, i);
            }
        }
        res.set_r_at(j, q);
    }
    return res;
}

int main(int argc, char **argv){
    int p[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    int p_length = sizeof(p) / sizeof(p[0]);
    int n = atoi(argv[1]);
    if(n < 1 || n > p_length){
        cout << "n debe ser menor o igual que " << p_length << " y mayor o igual que 1" << endl;
        exit(-1);
    }
    cout << "Memoized cut rod" << endl;
    cout << "r["<< n << "] = "<<memoized_cut_rod(p, n) << endl;
    cout << "Bottom-up cut rod" << endl;
    cout << "r["<< n << "] = "<< bottom_up_cut_rod(p, n) << endl;
    cout << "Extended bottom-up cut rod" << endl;
    Resultado res = extended_bottom_up_cut_rod(p, n);
    cout << "r["<< n << "] = "<< res.get_r_at(n) << endl;
    while(n > 0){
        cout << res.get_s_at(n - 1) << " ";
        n -= res.get_s_at(n - 1);
    }    
    return 0;   
}