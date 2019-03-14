#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char **argv)
{

  long len = atol(argv[1]);
  cout << "Entered " << len << endl;

  long *lens = new long[len+1];

  for (int i=1;i<len+1;++i) {
    lens[i] = 0;
  }

  int max_len = 0;
  int max_start = 0;
  for (int start=1;start<=len;++start) {
    long n = start;
    int l = 1;

    while (n != 1) {
      if (n < len && lens[n] > 0) {
	l += lens[n];
	n = 1;
      } else {
	if (n%2) {
	  n = 3*n + 1;
	} else {
	  n /= 2;
	}
	l += 1;
      }
    }
    lens[start] = l;
    
    if (l > max_len) {
      max_len = l;
      max_start = start;
    }
    
  }
  cout << "Max length sequence is " << max_len << " for " << max_start << endl;
  return 0;
}
// 113383
