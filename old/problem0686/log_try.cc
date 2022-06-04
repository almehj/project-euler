#include <iostream>
#include <cmath>
#include <climits>

using namespace std;

int main(int arc, char **argv)
{
  double log_2 = log10(2.);

  int n_max = atol(argv[1]);

  int p = 1;
  int n = 0;
  double log_lo = log10(1.23);
  double log_hi = log10(1.24);
    
  double log_n,log_m,intp;
    
  while (n < n_max) {
    double log_n = p * log_2;
    double log_m = modf(log_n,&intp);
    if ((log_m >= log_lo) && (log_m < log_hi)){
      n++;
      if (n%10000 == 0) {
	cout << "." << flush;
      }
    }
    p++;
  }

  cout << endl << n << " " << p - 1 << endl;
  
}

