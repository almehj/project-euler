#!/usr/bin/env python

import sys

class path_grid_analyzer(object):

    def __init__(self,infile_name):
        self.clear()
        self.ingest_file(infile_name)

    def clear(self):
        self.rows = []

    def ingest_file(self,infile_name):
        with open(infile_name,'r') as infile:
            for line in infile:
                if line.strip() == "": continue
                row = [int(s) for s in line.split()]
                if len(row) != (len(self.rows) + 1):
                    sys.stderr.write("Error reading %s: Row %s has %d values instead of expected %d"%(infile_name,len(self.rows),len(row),len(self.rows)+1))
                    self.clear()
                    return
                self.rows.append(row)
                



    def __str__(self):
        max_width = (2*len(self.rows) - 1)*2
        fmt_str = "{:^%ds}"%(max_width)
        row_strs = []
        for row in self.rows:
            row_str = "  ".join(["%02d"%(i) for i in row])
            row_strs.append(fmt_str.format(row_str))

        return '\n'.join(row_strs)
    
    def find_path(self):
        max_vals = [(n,[i]) for i,n in enumerate(self.rows[-1])]
        for row in reversed(self.rows[:-1]):
            new_max_vals = []

            print(max_vals)
                
            for i,n in enumerate(row):
                mi = i
                if n + max_vals[i][0] < n + max_vals[i+1][0]:
                    mi = i+1

                mv = n+max_vals[mi][0]
                mpath = [i] + max_vals[mi][1][:]

                new_max_vals.append(tuple([mv,mpath]))
            max_vals = new_max_vals

        print(max_vals)
        return max_vals[0]

    def print_path(self,path):

        max_width = (2*len(self.rows) - 1)*2
        fmt_str = "{:^%ds}"%(max_width)        
        for pi,row in zip(path,self.rows):
            row_bits = []
            for i,n in enumerate(row):
                if i == pi:
                    row_bits.append("*%02d*"%(n))
                else:
                    row_bits.append(" %02d "%(n))
            print(fmt_str.format(''.join(row_bits)))
                    
        

def main():
    for infile_name in sys.argv[1:]:
        print("Reading %s"%(infile_name))
        PG = path_grid_analyzer(infile_name)
        print("Grid:")
        print(PG)
        print("\n")
        max_path_val,max_path = PG.find_path()
        
        print("\n Largest total path has value %d"%(max_path_val))
        print(" Max path: %s"%(' '.join([str(i) for i in max_path])))
        PG.print_path(max_path)
        
if __name__ == "__main__":
    main()
