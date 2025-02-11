#include<iostream>
using namespace std;

int sMax(int arr[], int size){
    int max=0;
    int max2=0;
    for (int i = 0; i < size; i++){
        int val = arr[i];
        if (i > max){
            max = i;
        }

        else if(i > max2 and max != max2){
            max2 = i;
        }
        return max2;
    }
    return max2;
}

int main(){

    int arr[] = {1, 2, 3, 4, 5};
    cout << sMax(arr, 5) << endl;
}