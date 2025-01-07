/*Given an integer array nums and an int val, remove all occurnece of val in nums.
The order of elements may be changed. Then return the number of elements in nums which are not equal to val.
consider no of elements not equal to val as 'k', to get accepted, do the following
1. Change the array nums such that k elemenst of nums contain the lements which are not equal to val. 
2. return k. */
#include <iostream>
#include <vector>
using namespace std;

class Solution{
    public:
    int removeDuplicates(vector<int>& nums){
        int i=0;

        for (const int num:nums){
            if(i<1||num>nums[i-1]){
                nums[i++]=num;
        }
        return i;

    }
}
};

int main(){
    Solution solution;
    vector<int> test = {1,1,2,2,3,3,4,4,5,5};
    cout<<solution.removeDuplicates(test)<<endl;
    return 0;
}