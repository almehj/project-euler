#include <iostream>

using namespace std;

int main()
{
  unsigned long a = 1504170715041707;
  unsigned long dn = 8912517754604;
  
  unsigned long n = a;
  unsigned long coin = a;
  
  cout << a << " " << 0 << endl;

  while (n > 1) {

    n += dn;
    n %= a;

    if (n < coin) {
      unsigned long delta = coin - n;
      cout << n << " " << delta << endl << flush;      
      coin = n;
      while (n > delta) {
	n -= delta;
	cout << n << " " << delta << endl << flush;
	coin = n;
      }
    }
  }
}
