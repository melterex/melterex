#include <iostream>
#include <cmath>
using namespace std;

int fibonacci(int i) {
    if (i <= 1) return 1;
    else return fibonacci(i - 1) + fibonacci(i - 2);
}

int prod(int a) {
    if (a <= 1) return 1;
    else 
    return prod( a - 1 ) * fibonacci(a);
}

int main(void) {
    int n;
    cin>>n;
    cout << prod((n-1) % 10000000000) << endl;
    return 0;
}

