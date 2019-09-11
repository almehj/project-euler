#!/usr/bin/env python3

import sys

def gen_func(x,n):

    answer = 0 
    for i in range(n+1):
        answer += (-x)**i


    return answer

def base_mat(n):
    answer = []

    for i in range(n):
        row = [(i+1)**j for j in range(n)]
        answer.append(row)

    return answer

def scale_row(A,b,row_i,coeff):
    row = A[row_i]
    for i in range(len(row)):
        row[i] *= coeff
    b[row_i] *= coeff

    return A,b

def add_row(A,b,from_i,to_i,coeff=1):
    from_row = A[from_i]
    to_row = A[to_i]

    for i in range(len(to_row)):
        to_row[i] += coeff*from_row[i]
    b[to_i] += coeff*b[from_i]
    
    return A,b

def print_state(A,b):

    order = len(b)
    
    width = -1
    for row in A:
        row_width = len(str(max(row)))
        if row_width > width:
            width = row_width

    
    fmt = "%%%dd"%(width)

    orderwidth = len(str(order-1))
    order_fmt = " A%0%%dd "%(orderwidth)

    for i,row in enumerate(A):
        print(" ".join([fmt%n for n in row]+[order_fmt%(i)] + ["   ",str(b[i])]))
    

def eliminate(A,b,row_i,col_j):

    row = A[row_i]
    x = float(row[col_j])

    A,b = scale_row(A,b,row_i,1/x)

    for i in range(row_i+1,len(A)):
        coeff = A[i][row_i]
        A,b = add_row(A,b,row_i,i,-coeff)
    
    return A,b


def get_fit(A,b):
    order = len(b)
    for i in range(order):
        A,b = eliminate(A,b,i,i)
        b = [int(x) for x in b]

    a_vec = [0 for i in range(order)] 
    for i in reversed(range(order)):
        a_vec[i] = b[i]
        for j in range(i+1,order):
            a_vec[i] -= A[i][j]*a_vec[j]

    return a_vec


def eval_poly(a,x):

    answer = 0
    for i,a_i in enumerate(a):
        answer += a_i*x**i
    return answer

def do_search(max_order):

    tot_fit = 0
    for order in range(max_order):

        order += 1
        
        A = base_mat(order)
        b = [gen_func(i+1,max_order) for i in range(order)]
        print_state(A,b)

        
        a_vec = get_fit(A,b)
        print(a_vec)
        print(gen_func(1,max_order))
        print(int(eval_poly(a_vec,1)))
        
        n = 1
        while int(eval_poly(a_vec,n)) == gen_func(n,max_order):
            n += 1

        print(" ")
        fit = int(eval_poly(a_vec,n))

        print(fit)
        tot_fit += fit

    return tot_fit
        
    
        
        
def main():
    max_order = int(sys.argv[1])


    print(" ".join([str(gen_func(i,max_order)) for i in range(1,100)]))
    
    tot_fit = do_search(max_order)

    print("Total of FITs is %d"%(tot_fit))
        
        
if __name__ == "__main__":
    main()
