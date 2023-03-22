#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, k=1, n1=1, n2=1, i, buf;
    
    cin>>n;
    for(i=0; i < n; i++)
    {
        k = k * n1;
        buf = n1;
        n1 = n2;
        n2 = n2 + buf;
    }
    cout<<k / pow(10, 10);
    return 0;
}

