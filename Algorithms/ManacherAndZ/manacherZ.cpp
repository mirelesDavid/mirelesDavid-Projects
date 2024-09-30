#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string readFile(const string &filename) {
    ifstream file(filename);
    if (!file) {
        exit(1);
    }
    string content((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
    return content;
}

string preprocess(const string &text) {
    string processedText = "#";
    for (char character : text) {
        processedText += character;
        processedText += '#';
    }
    return processedText;
}

string manacher(const string &text) {   
    string processedText = preprocess(text);
    int n = processedText.size();
    vector<int> palindromeRadius(n, 0);
    int center = 0, right = 0;

    for (int idx = 0; idx < n; ++idx) {
        int mirrorIndex = 2 * center - idx;
        if (idx < right) {
            palindromeRadius[idx] = min(palindromeRadius[mirrorIndex], right - idx);
        }
        while (idx + palindromeRadius[idx] + 1 < n && idx - palindromeRadius[idx] - 1 >= 0 
            && processedText[idx + palindromeRadius[idx] + 1] == processedText[idx - palindromeRadius[idx] - 1]) {
            ++palindromeRadius[idx];
        }
        if (idx + palindromeRadius[idx] > right) {
            center = idx;
            right = idx + palindromeRadius[idx];
        }
    }

    int maxLen = 0, centerIndex = 0;
    for (int idx = 0; idx < n; ++idx) {
        if (palindromeRadius[idx] > maxLen) {
            maxLen = palindromeRadius[idx];
            centerIndex = idx;
        }
    }

    int start = (centerIndex - maxLen) / 2;
    return text.substr(start, maxLen);
}

vector<int> zAlgorithm(const string &patternWithText) {
    int n = patternWithText.size();
    vector<int> zValues(n, 0);
    int left = 0, right = 0;

    for (int idx = 1; idx < n; ++idx) {
        if (idx <= right) {
            zValues[idx] = min(right - idx + 1, zValues[idx - left]);
        }
        while (idx + zValues[idx] < n && patternWithText[zValues[idx]] == patternWithText[idx + zValues[idx]]) {
            ++zValues[idx];
        }
        if (idx + zValues[idx] - 1 > right) {
            left = idx;
            right = idx + zValues[idx] - 1;
        }
    }
    return zValues;
}

void highlightOccurrences(const string &text, const string &pattern) {
    string combinedText = pattern + "$" + text;
    vector<int> zValues = zAlgorithm(combinedText);
    int patternLength = pattern.size();

    ofstream htmlFile("highlight.html");
    htmlFile << "<html><body><p>";

    for (int idx = 0; idx < text.size(); ++idx) {
        bool found = false;
        if (zValues[idx + patternLength + 1] == patternLength) {
            htmlFile << "<span style='background-color: yellow'>" << text.substr(idx, patternLength) << "</span>";
            idx += patternLength - 1;
            found = true;
        }
        if (!found) {
            htmlFile << text[idx];
        }
    }

    htmlFile << "</p></body></html>";
    htmlFile.close();
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    string filename = argv[1];
    string text = readFile(filename);

    string longestPalindrome = manacher(text);
    cout << longestPalindrome << endl;

    highlightOccurrences(text, longestPalindrome);

    cout << "highlight.html Created" << endl;

    return 0;
}
