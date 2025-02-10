#include<iostream>
using namespace std;

int reverse(int n){
    if(n == 0){
        return 0;
    }

    else{
        int rev = 0;
        while(n != 0){
            rev = (rev*10) + (n%10);
            n = n/10;
        }
        return rev;

    }
}
int main() {
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    int rev = reverse(num);
    cout<<"Reverse of the number is: "<<rev;
}