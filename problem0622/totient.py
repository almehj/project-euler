#!/usr/bin/env python


import sys


def main():

    n_max = int(sys.argv[1])
    totient = {0: 0, 1: 1}

    n = 2
    while n <= n_max:
        if n not in totient:
            # Prime
            totient[n] = n-1
            k = 2
            while n*k <= n_max:
                if n*k not in totient:
                    totient[n*k] = []
                totient[n*k].append(n)
                k += 1
        else:
            tv = n
            for f in totient[n]:
                tv *= (1 - 1/f)
            totient[n] = int(tv)
        n += 1
    for n in range(n_max+1):
        print(n,totient[n])


if __name__ == "__main__":
    main()


