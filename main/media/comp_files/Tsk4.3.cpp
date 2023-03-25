#include <iostream>
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
    cout << prod(n-1) << endl;
    return 0;
}
