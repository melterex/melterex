#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long x1, x2;
    cin >> x1 >> x2;
    long long result = max(-(x1 + x2), x1 * x2);
    cout << result << endl;
    return 0;
}
#include <iostream>

// using namespace std;

// int main() {
//     int c1, c2;
//     cin >> c1 >> c2;
//     cout << 180 - c1 - c2 << endl;
//     return 0;
// }
// #include <iostream>
// #include <string>

// using namespace std;

// int main() {
//     string a;
//     getline(cin, a);
//     int count = 0;
//     for (int i = 0; i < a.length(); i++) {
//         if (a[i] == 'A' || a[i] == 'a') {
//             count++;
//         }
//     }
//     cout << count << endl;
//     return 0;
// }
// #include <iostream>
// #include <vector>
// #include <cmath>

// using namespace std;

// vector<long long> fib(int n) {
//     vector<long long> a = {1, 1};
//     for (int i = 0; i < n - 2; i++) {
//         a.push_back(a[a.size() - 1] + a[a.size() - 2]);
//     }
//     return a;
// }

// int main() {
//     int n;
//     cin >> n;
//     vector<long long> a = fib(n);
//     long long prod = 1;
//     for (int i = 0; i < a.size(); i++) {
//         prod *= a[i];
//         prod %= (long long)(pow(10, 10));
//     }
//     cout << prod << endl;
//     return 0;
// }