#include<iostream>
 using namespace std;
  int main() {
    int a;
    cin >> a;
    if (a%5 != 0) {
      cout << "Harganya jelek :(";
      return 0 ;
        }
    int b = a/250;
    cout << b << " llembar 250 ribuan"<< endl;
    int c = (a%250)/100;
    cout << c << " llembar 100 ribuan"<< endl;
    int d = ((a%250)%100)/50;
    cout << d << " llembar 50 ribuan"<< endl;
    int e = (((a%250)%100)%50)/10;
    cout << e << " llembar 10 ribuan"<< endl;
    int f = ((((a%250)%100)%50)%10)/5;
    cout << f << " llembar 5 ribuan";
  }