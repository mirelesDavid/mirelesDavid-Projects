#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

vector<int> calculateChange(vector<int>& coins, int change) {
    int numOfCoins = coins.size();
    vector<int> dp(change + 1, INT_MAX);
    vector<int> selectedCoin(change + 1, -1);

    dp[0] = 0;

    for (int i = 1; i <= change; ++i) {
        for (int j = 0; j < numOfCoins; ++j) {
            if (coins[j] <= i && dp[i - coins[j]] != INT_MAX) {
                if (dp[i] > dp[i - coins[j]] + 1) {
                    dp[i] = dp[i - coins[j]] + 1;
                    selectedCoin[i] = j;
                }
            }
        }
    }

    if (dp[change] == INT_MAX) {
        return vector<int>(numOfCoins, 0);
    }

    vector<int> result(numOfCoins, 0);
    int currentValue = change;

    while (currentValue > 0) {
        int index = selectedCoin[currentValue];
        result[index]++;
        currentValue -= coins[index];
    }

    return result;
}

int main(int argc, char* argv[]) {
    ifstream coinsFile(argv[1]);
    int numCoins;
    coinsFile >> numCoins;
    vector<int> coins(numCoins);

    for (int i = 0; i < numCoins; ++i) {
        coinsFile >> coins[i];
    }

    coinsFile.close();

    int price = stoi(argv[2]);
    int payment = stoi(argv[3]);

    int change = payment - price;
    vector<int> result = calculateChange(coins, change);

    ofstream outputFile("result.txt");
    for (int i = 0; i < numCoins; ++i) {
        outputFile << coins[i] << " " << result[i] << endl;
    }

    outputFile.close();

    cout << "Check 'result.txt' for Answer" << endl;

    return 0;
}
