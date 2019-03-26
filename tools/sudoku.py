#!/usr/bin/env python3

import logging
import itertools
import operator

import combinatorics

logging.basicConfig(level=logging.DEBUG)

# Hard Wired for 9x9 puzzles. 
_BOX_DIM = 3
_ROW_LEN = _BOX_DIM**2
_cross_line = "+-------+-------+-------+"
_line_format = "| %d %d %d | %d %d %d | %d %d %d |"


_row_ndx_set = []
_col_ndx_set = []
_box_ndx_set = []

for i in range(_ROW_LEN):
    _row_ndx_set += [(0,i)]
    _col_ndx_set += [(i,0)]
    _box_ndx_set += [(i//_BOX_DIM,i%_BOX_DIM)]

class area_iterator:

    def __init__(self,base_ndx,ndx_set):
        self.next_i = 0
        self.ndx_set = []
        for ndx in ndx_set:
            curr_ndx = tuple(map(operator.add,base_ndx,ndx))
            self.ndx_set += [curr_ndx]
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.next_i == len(self.ndx_set):
            raise StopIteration

        self.next_i += 1
        return self.ndx_set[self.next_i-1]

def get_row_iterator(base_ndx):
    i,j = base_ndx
    return area_iterator((i,0),_row_ndx_set)

def get_col_iterator(base_ndx):
    i,j = base_ndx
    return area_iterator((0,j),_col_ndx_set)

def get_box_iterator(base_ndx):
    i,j = base_ndx
    i = _BOX_DIM*(i//_BOX_DIM)
    j = _BOX_DIM*(j//_BOX_DIM)
    return area_iterator((i,j),_box_ndx_set)
    
def invert_known_vector(v):
    answer = []
    for n in range(1,_ROW_LEN+1):
        if n not in v:
            answer += [n]
    return answer

def compute_box_coords(i):
    box_i = i//_BOX_DIM
    box_j = i%_BOX_DIM

    return (box_i,box_j)

def compute_box_ndx(i,j):    
    return (i//3)*_BOX_DIM + j//3

def compute_box_grid_upper_left(n):
    i,j = compute_box_coords(n)
    return _BOX_DIM*i,_BOX_DIM*j

def union(ll):
    answer = []
    for l in ll:
        for i in l:
            if i not in answer:
                answer.append(i)
    return answer
        

class sudoku_puzzle(object):

    def __init__(self,lines):
        self.clear()
        self.parse_lines(lines)
        self.update_zeros()
        self.compute_all_possibles()

    def clear(self):
        self.grid = []
        self.grid_setup = False
        self.col_zeros = []
        self.row_zeros = []
        self.box_zeros = []
        self.zeros_setup = False
        self.possibles = {}
        self.done = []
        
    def parse_lines(self,lines):
        assert(len(lines) == _ROW_LEN)
        for line in lines:
            proc_line = line.strip()
            assert(len(proc_line) == _ROW_LEN)
            row = []
            for c in proc_line:
                row.append(int(c))                
            self.grid.append(row)
        self.grid_setup = True

                    
    def setup_zeros(self):
        if not self.grid_setup:
            return

        l = [[] for i in range(_ROW_LEN)]
        self.row_zeros = l[:]
        self.col_zeros = l[:]
        self.box_zeros = l[:]
            
    def update_zeros(self):
        logging.debug(" Finding zeros in grid")
        
        if not self.grid_setup:
            logging.debug("  Grid not set up")
            return

        if not self.zeros_setup:
            logging.debug("   Zero lists not set up. Initializing")
            self.setup_zeros()

        for i in range(_ROW_LEN):
            logging.debug("   Computing zeros for row %d"%(i))
            self.row_zeros[i] = self.find_area_zeros(get_row_iterator((i,0)))
            logging.debug("   Computing zeros for column %d"%(i))
            self.col_zeros[i] = self.find_area_zeros(get_col_iterator((0,i)))
            box_i,box_j = compute_box_grid_upper_left(i)
            logging.debug("   Computing zeros for box starting at %d,%d)"%
                          (box_i,box_j))
            self.box_zeros[i] = self.find_area_zeros(get_box_iterator((box_i,box_j)))


    def find_area_zeros(self,area_iter):

        non_zeros = []
        for i,j in area_iter:
            if self.grid[i][j] != 0:
                non_zeros += [self.grid[i][j]]

        return invert_known_vector(non_zeros)        
            
    def report_area_zeros(self,name,zero_set):
        print(" %s unknowns:"%(name))
        for i,row in enumerate(zero_set):
            print("  %d: %s "%(i," ".join([str(i) for i in row])))
        
    def report_zeros(self):
        for name,zero_set in [("Row",self.row_zeros),
                              ("Column",self.col_zeros),
                              ("Box",self.box_zeros)]:
            self.report_area_zeros(name,zero_set)
            print(" ")


    def compute_all_possibles(self):

        logging.debug("Computing possibles for whole grid")
        
        self.possibles = {}
        for i in range(_ROW_LEN):
            for j in range(_ROW_LEN):
                logging.debug(" Considering %d,%d"%(i,j))
                self.possibles[(i,j)] = self.compute_possibles((i,j))
                
    def compute_possibles(self,ndx):
        poss_list = []
        logging.debug("  Computing possible values for cell %d,%d"%ndx)

        i,j = ndx
        if self.grid[i][j] == 0:
            logging.debug("   Unknown")
            
            box_i = compute_box_ndx(i,j)

            logging.debug("  (%d,%d) is in box %d (box coords %d,%d)"%
                          (i,j,box_i,box_i//_BOX_DIM,box_i%_BOX_DIM))
            logging.debug("        row_zeros[%d] == [%s]"%
                          (i," ".join([str(n) for n in self.row_zeros[i]])))
            logging.debug("        col_zeros[%d] == [%s]"%
                          (j," ".join([str(n) for n in self.col_zeros[j]])))
            logging.debug("        box_zeros[%d] == [%s]"%
                          (box_i," ".join([str(n) for n in self.box_zeros[box_i]])))

            for n in range(1,_ROW_LEN+1):
                if n in self.row_zeros[i] and \
                   n in self.col_zeros[j] and \
                   n in self.box_zeros[box_i]:
                    poss_list += [n]                            
        else:
            logging.debug("   Determined to be %d"%(self.grid[i][j]))

        logging.debug("   Possible list: %s"%(" ".join([str(n) for n in poss_list])))
        return poss_list

        
    def report_possibles(self):
        for i in range(_ROW_LEN):
            for j in range(_ROW_LEN):
                if self.grid[i][j] == 0:
                    print("%d,%d: %s"%
                          (i,j," ".join([str(n) for n in self.possibles[(i,j)]])))
                else:
                    print("%d,%d: DETERMINED %d"%(i,j,self.grid[i][j]))
    
    def __str__(self):
        lines = [_cross_line]
        for i in range(_BOX_DIM):
            for j in range(_BOX_DIM):
                line_i = 3*i + j
                lines.append(_line_format%tuple(self.grid[line_i]))
            lines.append(_cross_line)
        return '\n'.join(lines)


    def set_value(self,ndx,n,**kwargs):

        if n not in self.possibles[ndx]:
            logging.severe(" %d not in set of possibles for %d,%d, ignoring"%(n,i,j))
            raise RuntimeError("Attempt to set impossible value in cell")

        i,j = ndx

        if self.grid[i][j] != 0:
            logging.severe(" %d,%d already set to %d"%(i,j,self.grid[i][j]))
            raise RuntimeError("Attempt to set already-set cell")
        else:
            self.grid[i][j] = n

        # Update zero info
        box_i = compute_box_ndx(i,j)
        for l in [self.row_zeros[i], self.col_zeros[j], self.box_zeros[box_i]]:
            if n in l:
                l.remove(n)

        # Update possibles
        self.possibles[ndx] = []
        for area_iter_gen in [get_row_iterator,get_col_iterator,get_box_iterator]:
            area_iter = area_iter_gen((i,j))
            for ndx in area_iter:
                if n in self.possibles[ndx]:
                    self.possibles[ndx].remove(n)                    

    def solve(self):

        logging.debug("Considering Solution of grid")

        n = 0
        last_n = 1
        while n+last_n > 0:
            last_n = n
            n = 0
            n += self.do_unique_possible_analysis()
            n += self.do_singleton_analysis()
            n += self.do_cluster_analysis()

            

    def do_singleton_analysis(self):

        logging.debug(" Singleton analysis")
        
        n_replaced = 0

        n = self.do_singleton_pass()
        while n > 0:
            logging.debug("  Pass replaced %d"%(n))
            n_replaced += n
            n = self.do_singleton_pass()

        logging.debug(" Singleton analysis found %d new cell values"%(n_replaced))
        return n_replaced
            
    
    def do_singleton_pass(self):        

        logging.debug("   Considering singleton possibles")
        
        singletons = [ndx for ndx in self.possibles if len(self.possibles[ndx]) == 1]
        logging.debug("    %d cells with singleton possible list"%(len(singletons)))
        if len(singletons) > 0:
            logging.debug("    Singleton cells: %s"%
                          (" ".join([str(ndx) for ndx in singletons])))
            for ndx in singletons:
                i,j = ndx
                n = self.possibles[ndx][0]
                logging.debug("     Setting %d,%d to %d"%(i,j,n))

                self.set_value(ndx,self.possibles[ndx][0])

            logging.debug("     Set %d values"%(len(singletons)))
            
        # Tell caller how many, if any, cells we updated        
        return len(singletons)


    def do_unique_possible_analysis(self):

        logging.debug(" Unique possible analysis")

        n_replaced = 0

        n = self.do_unique_possible_pass()
        while n > 0:
            logging.debug("  Pass replaced %d"%(n))
            n_replaced += n
            n = self.do_unique_possible_pass()

        logging.debug(" Unique possible analysis found %d new cell values"%(n_replaced))
        return n_replaced
    
    def do_unique_possible_pass(self):

        logging.debug("   Considering possibles unique to a cell in a row|column|box")
        
        n_replaced = 0
        for n in range(_ROW_LEN):
            for area_iter in [
                    get_row_iterator((n,0)),
                    get_col_iterator((0,n)),
                    get_box_iterator(compute_box_grid_upper_left(n))
            ]:
                n_replaced += self.do_area_unique_possible_area_pass(area_iter)

        return n_replaced
    
    def do_area_unique_possible_area_pass(self,area_iter):
        n_replaced = 0
        cells_with_possible = {}
        for ndx in area_iter:
            i,j = ndx
            if self.grid[i][j] == 0:                
                for n in self.possibles[ndx]:
                    if n not in cells_with_possible:
                        cells_with_possible[n] = []
                    cells_with_possible[n] += [ndx]

        for n in cells_with_possible:
            if len(cells_with_possible[n]) == 1:
                self.set_value(cells_with_possible[n][0],n)
                n_replaced += 1

        return n_replaced
        
    def do_cluster_analysis(self):
        
        logging.debug(" Considering clusters in possibles")

        n_replaced = 0

        n = self.do_cluster_analysis_pass()
        while n > 0:
            n_replaced += n
            n = self.do_cluster_analysis_pass()
            
        # Return some indication we did something, or 0 if not
        logging.debug(" Cluster analysis found %d possibles to kill"%(n_replaced))
        return n_replaced

    def do_cluster_analysis_pass(self):

        logging.debug("   Considering clusters")
        
        n_replaced = 0
        for n in range(_ROW_LEN):
            for area_iter in [
                    get_row_iterator((n,0)),
                    get_col_iterator((0,n)),
                    get_box_iterator(compute_box_grid_upper_left(n))
            ]:
                for order in [2,3,4]:
                    n_replaced += self.do_area_cluster_analysis(area_iter,order)

        return n_replaced
        
    def do_area_cluster_analysis(self,area_iter,order):

        logging.debug("     Seeking clusters of size %d"%(order))

        n_replaced = 0
        possible_ndx_set = []
        ndx_set = []
        
        for ndx in area_iter:
            ndx_set += [ndx]
            i,j = ndx
            if self.grid[i][j] == 0 and len(self.possibles[ndx]) <= order:                
                possible_ndx_set += [ndx]

        if len(possible_ndx_set) >= order:
            C = combinatorics.combinator(possible_ndx_set,order)
            for curr_set in C:
                possible_union = union([self.possibles[i] for i in curr_set])
                if len(possible_union) == order:
                    logging.debug("       A possible cluster %s"%(str(possible_union))) 
                    # noone else can use these possibles
                    for ndx in ndx_set:
                        if ndx not in curr_set: 
                            for n in possible_union:
                                if n in self.possibles[ndx]:
                                    logging.debug("        Removing possible %d from %d,%d"%
                                                  (n,ndx[0],ndx[1]))
                                    self.possibles[ndx].remove(n)
                                    n_replaced += 1

                        
        return n_replaced
        
    def count_zeros(self):
        self.zeros_left = 0
        for i,j in itertools.product(range(_ROW_LEN),range(_ROW_LEN)):
            if self.grid[i][j] == 0:
                self.zeros_left += 1

    def is_solved(self):
        self.count_zeros()
        return self.zeros_left == 0

def main():
    i = int(sys.argv[1])
    j = int(sys.argv[2])

    for name,func in [
            ('Row',get_row_iterator),
            ('Col',get_col_iterator),
            ('Box',get_box_iterator)
    ]:
        ndx_iter = func((i,j))
        print("%s: %s"%(name," ".join([str(i) for i in ndx_iter])))
    
if __name__ == "__main__":
    import sys
    main()
    
