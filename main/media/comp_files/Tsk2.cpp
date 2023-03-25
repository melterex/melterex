#include <iostream>

using namespace std;

int main()
{
    int x1, x2, b, c;
    cin>> x1 >> x2;
    b = -1 * (x1 + x2);
    c = x1 * x2;
    if( b > c)
    {
        cout<< b;
    }
    else
    {
        cout<< c;
    }
    return 0;
}

