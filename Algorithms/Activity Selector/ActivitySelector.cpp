#include <iostream>
#include <vector>

using namespace std;

class Activity {
    private:
        int s; 
        int f; 

    public:
        Activity(int start, int finish) : s(start), f(finish) {}

        int get_s() const { return s; }
        int get_f() const { return f; }
};

vector<Activity> greedy_activity_selector(vector<Activity>& S) {
    int sLength = S.size();
    vector<Activity> answer;

    answer.push_back(S[0]);
    int k = 0;

    for (int m = 1; m < sLength; m++) {
        if (S[m].get_s() >= S[k].get_f()) {
            answer.push_back(S[m]);
            k = m;
        }
    }

    return answer;
}

int main() {
    vector<Activity> S;
    S.push_back(Activity(1, 4));
    S.push_back(Activity(3, 5));
    S.push_back(Activity(0, 6));
    S.push_back(Activity(5, 7));
    S.push_back(Activity(3, 9));
    S.push_back(Activity(5, 9));
    S.push_back(Activity(6, 10));
    S.push_back(Activity(8, 11));
    S.push_back(Activity(8, 12));
    S.push_back(Activity(2, 14));
    S.push_back(Activity(12, 16));

    vector<Activity> A = greedy_activity_selector(S);

    for (int i = 0; i < A.size(); i++) {
        cout << "s = " << A[i].get_s() << ", f = " << A[i].get_f() << endl;
    }

    return 0;
}
