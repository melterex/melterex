#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a;
    int i, k=0;
    getline(cin, a);
    
    for(i=0; i < a.length(); i++)
    {
        if(a[i]=='a' or a[i]=='A')
        k++;
    }
    cout<<k;
    return 0;
}

