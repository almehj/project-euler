#include <iostream>

using namespace std;

int main(int argc,char **argv)
{
  unsigned int n_max = atol(argv[1]);
  unsigned int f_max = atol(argv[2]);
  
  cout << n_max << " mod " << f_max << endl;

  int *table = new int[n_max+1];

  for (int i=0;i<=n_max;i++){
    table[i] = 1;
  }
  int n = 1;
  while (n <= n_max) {
    n++;
    for (int i=n;i<=n_max; i++) {
      table[i] += table[i-n];
      table[i] %= f_max;
      if (i == n) {
	if (table[n] == 0) {
	  cout << n << " " << table[n] << endl;
	  exit(0);
	}
      }
    }
  }
}
