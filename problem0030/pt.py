import sys


semifac = lambda n:1 if n<2 else n*semifac(n-2)

pi = lambda m: lambda n: 2*(10**m) if n==0 else (10**m)*semifac(2*n)//((2**(n-1))*semifac(2*n+1)) + pi(m)(n-1)

n = str(pi(10000)(200))

sys.stdout.write("%c."%(n[0]))
for i,c in enumerate(n[1:]):
    if i%10 == 0:
        sys.stdout.write(" ")
        sys.stdout.flush()
    sys.stdout.write("%c"%(c))
        
     
