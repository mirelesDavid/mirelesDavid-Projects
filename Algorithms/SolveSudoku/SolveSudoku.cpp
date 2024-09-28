#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

#define N 9

void printBoard(int board[N][N]) {
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++) {
            cout << board[row][col] << " ";
        }
        cout << endl;
    }
}

bool validAddition(int board[N][N], int row, int col, int num) {
    for (int x = 0; x < N; x++) {
        if (board[row][x] == num)
            return false;
    }

    for (int x = 0; x < N; x++) {
        if (board[x][col] == num)
            return false;
    }

    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i + startRow][j + startCol] == num)
                return false;
        }
    }

    return true;
}

bool solveSudoku(int board[N][N]) {
    int row, col;
    bool empty = false;

    for (row = 0; row < N; row++) {
        for (col = 0; col < N; col++) {
            if (board[row][col] == 0) {
                empty = true;
                break;
            }
        }
        if (empty)
            break;
    }

    if (!empty)
        return true;

    for (int num = 1; num <= 9; num++) {
        if (validAddition(board, row, col, num)) {
            board[row][col] = num;

            if (solveSudoku(board))
                return true;

            board[row][col] = 0;
        }
    }

    return false;
}

int main(int argc, char *argv[]) {
    int board[N][N];
    ifstream inputFile(argv[1]);

    if (inputFile.is_open()) {
        string line;
        int row = 0;
        while (getline(inputFile, line)) {
            if (line.find("INICIO DE ARCHIVO") != string::npos || line.find("FIN DE ARCHIVO") != string::npos) {
                continue;
            }

            if (row < N) {
                stringstream ss(line);
                string value;
                int col = 0;
                while (getline(ss, value, ',')) {
                    board[row][col] = stoi(value);
                    col++;
                }
                row++;
            }
        }
        inputFile.close();
    } else {
        cout << "Could not open the file" << endl;
        return 1;
    }

    if (solveSudoku(board)) {
        printBoard(board);

        ofstream outputFile("solution.txt");
        if (outputFile.is_open()) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    outputFile << board[i][j];
                    if (j < N - 1)
                        outputFile << ", ";
                }
                outputFile << endl;
            }
            outputFile.close();
        } else {
            cout << "Could not open the output file" << endl;
        }
    } else {
        cout << "No solution for this Sudoku" << endl;
    }

    return 0;
}
