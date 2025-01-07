//Write a fn to find the 

#include <iostream>
#include <stack>
#include <string> // Include string for compatibility
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (const char c : s) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.empty() || stack.top() != c) {
                return false;
            } else {
                stack.pop();
            }
        }
        return stack.empty();
    }
};

int main() {
    Solution solution;
    string test = "()[]{}";
    if (solution.isValid(test)) {
        cout << "Valid" << endl;
    } else {
        cout << "Invalid" << endl;
    }
    return 0;
}
