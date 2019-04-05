#!/usr/bin/env python3

import sys

import utils

class set_generator:

    def __init__(self,n):
        self.digits = [0]*n
        self.digits[0] = 1
        self.curr_len = 1
        self.done = False
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration

        answer = self.digits[:self.curr_len][:]

        end_ndx = self.curr_len - 1
        self.digits[end_ndx] += 1

        i = end_ndx
        while i >= 0 and self.digits[i] == 9:
            i -= 1

        if i > 0:
            self.digits[i] = self.digits[i-1]+1
            for j in range(i+1,self.curr_len):
                self[j] = self[j-1]
        elif i == 0:
            self.curr_len += 1
            for j in range(self.curr_len):
                self.digits[j] = 1
        else:
            self.done = True
            
            
        return answer

        
                            

                
                
            
            
        if self.digits[end_ndx] > 9:
            self.done = True
            

        return answer
    
def main():

    max_len = int(sys.argv[1])

    s = set_generator(max_len)

    for t in s:
        print(utils.seq_string(t))


if __name__ == "__main__":
    main()
