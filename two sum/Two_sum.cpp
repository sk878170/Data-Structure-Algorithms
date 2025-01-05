//Given an array of integers nums and an integer target, return indices of two numbers such that they add up to a target.
// Assume that each input would have exactly one solution and you cannot use same element twice.

#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

vector<int> twoSum(vector<int>& nums,int target){
    unordered_map<int,int> map;
    for (int i=0; i<nums.size();i++){
        int complement = target - nums[i];
        if (map.find(complement) !=map.end()){
            return{map[complement],i};
        }
        map[nums[i]] = i;
        
    }
    return {};
}

int main(){
    int n, target;
    cout<<"Enter the number of elements:";
    cin>>n;

    vector<int> nums(n);
    cout<<"Enter the elements:";
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }

    vector<int> result=twoSum(nums,target);

    if(!result.empty()){
        cout<<"Indices of two numbers that add up to "<<target<<" are "<<result[0]<<endl;
    }
    else{ 
        cout<<"No solution found";
    }
}