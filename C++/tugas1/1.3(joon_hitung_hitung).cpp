#include<iostream>
 using namespace std;
  int main() {
    int a, b;
    int c = 0;
    cin >> a >> b;
    for (int j = a;j <= b;j++) {
      if (j%2==1) {
        c += j;
      }
    }
    cout << c;
  }