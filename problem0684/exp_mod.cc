#include<iostream>

using namespace std;

unsigned long exp_squaring(unsigned long b,
			   unsigned long e,
			   unsigned long m)
{
  if (e < 0) {
    return exp_squaring(b,-e,m);
  }

  if (e == 0) {
    return 1;
  }

  if (e%2 == 0) {
    return exp_squaring((b*b)%m,e/2,m);
  } else {
    return (b * exp_squaring((b*b)%m,(e-1)/2,m))%m;
  }
}

unsigned long power(unsigned long b,
		    unsigned long e,
		    unsigned long m)
{
  return exp_squaring(b,e,m);
}


#ifdef DRIVER
int main(int argc, char **argv)
{
  unsigned long b = atol(argv[1]);
  unsigned long e = atol(argv[2]);
  unsigned long m = atol(argv[3]);
    
  cout << b << "^" << e << " = " << power(b,e,m) << " mod " << m << endl;
}
#endif // DRIVER
