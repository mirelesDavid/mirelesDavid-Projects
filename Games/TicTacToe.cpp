#include <iostream>
#include <cstdlib>
#include <ctime>
#include <conio.h>
#include <windows.h>

using namespace std;

bool gameOver, madeMove = false;
char board[3][3];
int answ;

void setUp() {
    gameOver = false;
    srand(time(0));
    answ = rand() % 2;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

void drawMap() {
    system("CLS");

    if (answ == 1) {
        cout << "TURNO JUGADOR X." << endl;
    } else {
        cout << "TURNO JUGADOR O" << endl;
    }

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (j > 0) {
                cout << "|";
            }
            cout << " " << board[i][j] << " ";
        }
        cout << endl;

        if (i < 2) {
            cout << "------------" << endl;
        }
    }
}

void input() {
    if (!madeMove) {
        if (_kbhit()) {
            char key = _getch();
            switch (key) {
                case 'q':
                    board[0][0] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'w':
                    board[0][1] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'e':
                    board[0][2] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'a':
                    board[1][0] = (answ == 1) ? 'X' : 'O';
                    break;
                case 's':
                    board[1][1] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'd':
                    board[1][2] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'z':
                    board[2][0] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'x':
                    board[2][1] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'c':
                    board[2][2] = (answ == 1) ? 'X' : 'O';
                    break;
                case 'm':
                    gameOver = true;
                    break;
            }
            madeMove = true;
            
        }
    }
}void Logic() {
    if (!madeMove) {
        return; 
    }

    bool winnerFound = false;

    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') ||
            (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ')) {
            gameOver = true;
            cout << ((answ == 1) ? 'X' : 'O') << " gana " << endl;
            winnerFound = true;
            break;
        }
    }

    if (!winnerFound) {
        if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') ||
            (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ')) {
            gameOver = true;
            cout << ((answ == 1) ? 'X' : 'O') << " gana " << endl;
            winnerFound = true;
        }
    }

    if (!winnerFound) {
        bool isFull = true;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    isFull = false;
                    break;
                }
            }
        }

        if (isFull) {
            gameOver = true;
            cout << " Empate " << endl;
        }
    }

    if (madeMove && !winnerFound) {
        answ = (answ == 1) ? 0 : 1;
        madeMove = false;
    }
}



int main() {
    setUp();
    while (!gameOver) {
        drawMap();
        if (!gameOver) {
            input();
            Logic();
        }
        Sleep(269);
    }
    return 0;
}