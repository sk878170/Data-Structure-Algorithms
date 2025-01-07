/*Given an integer array nums and an int val, remove all occurnece of val in nums.
The order of elements may be changed. Then return the number of elements in nums which are not equal to val.
consider no of elements not equal to val as 'k', to get accepted, do the following
1. Change the array nums such that k elemenst of nums contain the lements which are not equal to val. 
2. return k. */


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeOccurrences(vector<int>& nums, int val) {
        int k = 0; // Pointer for valid elements

        for (int num : nums) {
            if (num != val) {
                nums[k++] = num; // Keep elements that are not equal to val
            }
        }
        return k; // Number of elements not equal to val
    }
};

int main() {
    Solution solution;
    vector<int> nums;
    int n, val;

    // Input the size of the array
    cout << "Enter the size of the array: ";
    cin >> n;

    // Input the array elements
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; ++i) {
        int element;
        cin >> element;
        nums.push_back(element);
    }

    // Input the value to remove
    cout << "Enter the value to remove: ";
    cin >> val;

    // Remove occurrences of the value
    int k = solution.removeOccurrences(nums, val);

    // Output the result
    cout << "Number of elements after removal: " << k << endl;
    cout << "Modified array: ";
    for (int i = 0; i < k; ++i) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}
