#include<iostream>

using namespace std;


unsigned long power(unsigned long,unsigned long,unsigned long);

const int N_MAX = 100;
const unsigned long w_modulus = 1000000007;

unsigned long *fibs;

void init_fibs() {
  fibs = new unsigned long[N_MAX];
  for (int i=0; i<N_MAX; i++) {
    fibs[i] = 0;
  }
  fibs[0] = 0;
  fibs[1] = 1;
}

unsigned long fib(int n) {
 
  if (n < 2 || fibs[n] > 0) {
    return fibs[n];
  }

  fibs[n] = fib(n-1) + fib(n-2);
  return fibs[n];
}

unsigned long s(unsigned long n)
{
  unsigned long n_nines = n/9;
  int l = n%9;

  unsigned long tens = power(10,n_nines,w_modulus);

  return ((l+1)*tens - 1)%w_modulus;
}

unsigned long big_s(unsigned long n)
{
  unsigned int n_segs = n/9;
  unsigned int base = power(10,n_segs,w_modulus);
  base = 5*base;
  base = base - (5 + n_segs*9)%w_modulus;
  base %= w_modulus;

  unsigned int r = n_segs*9;
  while (r <= n) {
    base += s(r);
    base %= w_modulus;
    r++;
  }

  return base;  
}

int main(int argc, char **argv)
{

  init_fibs();
  
  int n_max = atol(argv[1]);

  cout << n_max << " " << big_s(n_max) << endl << endl; 
  
  unsigned long total = 0;
  for (int n=1; n<=n_max;n++) {
    unsigned long fn = fib(n);
    unsigned long sn = big_s(fn);
    total += sn;
    total %= w_modulus;

    cout << n << " " << fn << " " << sn << " " << total << endl;
  }
  cout << endl;
  cout << "Total for 2 to " << n_max << " is " << total - 1 << endl; 
}
