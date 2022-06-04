#!/usr/bin/env python


def other_digit(t,n):
    if n == t[0]:
        return t[1]
    else:
        return t[0]



big_n = 1
big_d = 1

for num in range(11,100):
    for den in range(num+1,100):

        num_digits = num//10,num%10
        den_digits = den//10,den%10

        commons = []
        for i in range(2):
            if num_digits[i] in den_digits:
                if num_digits[i] not in commons:
                    commons.append(num_digits[i])
        if len(commons) == 1 and commons[0] != 0:
            num_d = other_digit(num_digits,commons[0])
            den_d = other_digit(den_digits,commons[0])

            if num_d*den_d > 0 and num_d/den_d < 1.:
                if num*den_d == den*num_d:
                    print("%d/%d: %s"%(num,den,commons))
                
                    big_n *= num_d
                    big_d *= den_d


print("%d/%d"%(big_n,big_d))


