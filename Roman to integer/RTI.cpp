#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    // Function to convert Roman numeral to integer
    int romantoInt(string s) {
        unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int total = 0;
        int prev = 0;

        // Traverse the Roman numeral in reverse order
        for (int i = s.length() - 1; i >= 0; i--) {
            int value = roman[s[i]];
            if (value < prev) {
                total -= value;
            } else {
                total += value;
            }
            prev = value;
        }
        return total;
    }

    // Function to convert integer to Roman numeral
    string inttoRoman(int num) {
        unordered_map<int, string> roman = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
                                             {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
                                             {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};

        string result = "";
        // Traverse through the Roman numeral values in descending order
        for (auto it = roman.begin(); it != roman.end(); ++it) {
            while (num >= it->first) {
                result += it->second;
                num -= it->first;
            }
        }
        return result;
    }
};

int main() {
    Solution sol;
    string ans = "y";

    while (ans == "y") {
        cout << "Menu\n1. Roman to Integer\n2. Integer to Roman\n";
        int choice;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            string roman_number;
            cout << "Enter the Roman number: ";
            cin >> roman_number;
            int result = sol.romantoInt(roman_number);
            cout << "The integer value of " << roman_number << " is: " << result << endl;
        } else if (choice == 2) {
            int integer_number;
            cout << "Enter the integer: ";
            cin >> integer_number;
            string result = sol.inttoRoman(integer_number);
            cout << "The Roman numeral for " << integer_number << " is: " << result << endl;
        } else {
            cout << "Invalid choice!" << endl;
        }

        cout << "Quit [y/n]: ";
        cin >> ans;
    }

    return 0;
}
