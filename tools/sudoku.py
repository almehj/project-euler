#!/usr/bin/env python3

import logging
import itertools
import operator
import sys

import combinatorics
from utils import seq_string

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

    def __str__(self):
        lines = [_cross_line]
        for i in range(_BOX_DIM):
            for j in range(_BOX_DIM):
                line_i = 3*i + j
                lines.append(_line_format%tuple(self.grid[line_i]))
            lines.append(_cross_line)
        return '\n'.join(lines)

    def as_lines(self):
        return ["".join([str(i) for i in row]) for row in self.grid]
        
    def clear(self):
        self.grid = []
        self.grid_setup = False
        self.col_zeros = []
        self.row_zeros = []
        self.box_zeros = []
        self.zeros_setup = False
        self.possibles = {}
        self.done = []
        self.name = "No name"
        
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
            logging.debug("   Computing zeros for box starting at (%d,%d)"%
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
    
    def set_value(self,ndx,n,**kwargs):

        i,j = ndx

        if n not in self.possibles[ndx]:
            logging.warn(" %d not in set of possibles for %d,%d, death!!!!"%(n,i,j))
            return False
        
        if self.grid[i][j] != 0:
            logging.warn(" %d,%d already set to %d"%(i,j,self.grid[i][j]))
            return False
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
            for poss_ndx in area_iter:
                if n in self.possibles[poss_ndx]:
                    self.possibles[poss_ndx].remove(n)
                if not self.is_possible():
                    logging.warn("  Setting cell %d,%d to %d eliminates last possible for cell %d,%d"%\
                                 (poss_ndx[0],poss_ndx[1],n,i,j))

        # OK
        return True
                    
    def get_value(self,ndx):
        i,j = ndx
        return self.grid[i][j]

    def count_zeros(self):
        self.zeros_left = 0
        for i,j in itertools.product(range(_ROW_LEN),range(_ROW_LEN)):
            if self.grid[i][j] == 0:
                self.zeros_left += 1

    def is_solved(self):
        self.count_zeros()
        return self.zeros_left == 0


    def is_possible(self):
        return len(self.get_cells_by_n_possible(0)) == 0
    
    def get_cells_by_n_possible(self,n):
        answer = []
        for ndx in itertools.product(range(_ROW_LEN),range(_ROW_LEN)):
            if self.grid[ndx[0]][ndx[1]] == 0:
                if len(self.possibles[ndx]) == n:
                    answer += [ndx]
        return answer

    def get_unset_cells(self):
        answer = []
        for ndx in itertools.product(range(_ROW_LEN),range(_ROW_LEN)):
            if self.get_value(ndx) == 0:
                answer += [ndx]
        return answer







    
    def solve(self):

        logging.debug("Considering Solution of Puzzle %s"%(self.name))
        self.try_logic_solution()

        if self.is_solved():
            logging.debug(" Pure logic solved %s"%self.name)
            return
        else:
            logging.debug(" Pure logic did not solve %s"%self.name)

        self.try_speculative_solution()
        if self.is_solved():
            logging.debug(" Guess and check solved %s"%self.name)
            return
        else:
            logging.debug(" Guess and check did not solve %s"%self.name)
            logging.debug(" I give up")
        
    def try_logic_solution(self):
        logging.debug(" Applying pure logical solution methods")

        n = 0
        last_n = 1
        while n+last_n > 0 and self.is_possible():
            last_n = n
            n = 0
            for solver in [self.do_unique_possible_analysis,
                           self.do_singleton_analysis,
                           self.do_cluster_analysis,
                           self.do_unique_cross_analysis]:
                curr_n = solver()
                if self.is_possible():
                    n += curr_n
                else:
                    logging.warn("  Last operation rendered puzzle unsolvable.")
                    return
            n += len(self.get_cells_by_n_possible(1))
        return

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
        n_set = 0
        if len(singletons) > 0:
            logging.debug("    Singleton cells: %s"%
                          (" ".join([str(ndx) for ndx in singletons])))
            for ndx in singletons:
                if len(self.possibles[ndx]) == 0:
                    logging.warn(" No possibles for cell %d,%d"%ndx)
                    break
                
                i,j = ndx
                n = self.possibles[ndx][0]
                logging.debug("     Setting %d,%d to %d"%(i,j,n))

                if not self.set_value(ndx,self.possibles[ndx][0]):
                    if not self.is_possible():
                        logging.warn("Puzzle is in unsolvable state")
                    else:
                        logging.warn("Could not set singleton value %d in cell %d,%d"%\
                                     (self.possibles[ndx][0],i,j))
                    break
                else:
                    n_set += 1
                    
            logging.debug("     Set %d values"%(n_set))
            
        # Tell caller how many, if any, cells we updated        
        return n_set


    def do_unique_possible_analysis(self):

        logging.debug(" Unique possible analysis")

        n_set = 0

        n = self.do_unique_possible_pass()
        while n > 0:
            logging.debug("    Pass replaced %d"%(n))
            n_set += n
            n = self.do_unique_possible_pass()

        logging.debug(" Unique possible analysis found %d new cell values"%(n_set))
        
        return n_set
    
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
                if not self.is_possible():
                    return n_replaced

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
            if not self.is_possible():
                logging.warn("Previous value eliminated last possible value for cell %d,%d"%ndx)
                break

            if len(cells_with_possible[n]) == 1:                
                ndx = cells_with_possible[n][0]
                
                if self.set_value(ndx,n):
                    n_replaced += 1
                else:
                    logging.warn(" Puzzle is in unsolvable state")
                    break

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



    def do_unique_cross_analysis(self):
        logging.debug(" Applying unique cross solution techniques")

        n_eliminated = 0

        n = 1
        curr_n = 0
        while n + curr_n > 0:
            n_eliminated += curr_n
            n = curr_n
            curr_n = 0
            for i in range(_ROW_LEN):
                curr_n += self.do_unique_cross_analysis_pass(get_row_iterator((i,0)))
                curr_n += self.do_unique_cross_analysis_pass(get_col_iterator((0,i)))

        logging.debug(" Unique cross pass eliminated %d possibles"%(n_eliminated))            
        return n_eliminated
                                                             
                                                            
    def do_unique_cross_analysis_pass(self,it):

        n_eliminated = 0

        possible_secs = {}
        sec_cells = [[] for i in range(_BOX_DIM)]
        
        for i,ndx in enumerate(it):
            sec_ndx = i//_BOX_DIM
            sec_cells[sec_ndx].append(ndx)
            for val in self.possibles[ndx]:
                if val not in possible_secs:
                    possible_secs[val] = []
                if sec_ndx not in possible_secs[val]:
                    possible_secs[val].append(sec_ndx)

        for val in possible_secs:
            if len(possible_secs[val]) == 1:
                sec_ndx = possible_secs[val][0]
                logging.debug("  Value %d uniqe to section in box containing %s"% \
                              (val,str(sec_cells[sec_ndx])))

                for ndx in get_box_iterator(sec_cells[sec_ndx][0]):
                    if not ndx in sec_cells[sec_ndx]:
                        if val in self.possibles[ndx]:
                            self.possibles[ndx].remove(val)
                            n_eliminated += 1

                            logging.debug("    Removed possible %d from %s leaving %s"%\
                                          (val,str(ndx),str(self.possibles[ndx])))
                            

        return n_eliminated
    
    def old_do_cluster_analysis_pass(self):
        n_eliminated = 0
        
        for row_ndx in range(_ROW_LEN):
            uniques = [[] for i in range(_BOX_DIM)]
            for test_val in range(1,_ROW_LEN+1):
                sec_with_val = []
                for sec_ndx in range(_BOX_DIM):
                    col_ndxs = [i for i in range(_BOX_DIM*sec_ndx,_BOX_DIM*(sec_ndx+1))]
                    for col_ndx in col_ndxs:
                        ndx = (row_ndx,col_ndx)
                        if test_val in self.possibles[ndx]:
                            sec_with_val += [sec_ndx]
                            break
                if len(sec_with_val) == 1:
                    logging.debug("    Found value %d is unique in row %d, section %d"%\
                                  (test_val,row_ndx,sec_with_val[0]))
                    base_ndx = (row_ndx,_BOX_DIM*sec_with_val[0])
                    area_iter = get_box_iterator(base_ndx)
                    for ndx in area_iter:
                        if ndx[0] == row_ndx or self.grid[ndx[0]][ndx[1]] != 0:
                            continue
                        if test_val in self.possibles[ndx]:
                            self.possibles[ndx].remove(test_val)
                            n_eliminated += 1

        logging.debug(" Unique cross eliminated %d possibles"%(n_eliminated))
        return n_eliminated
    
    def try_speculative_solution(self):
        return
        logging.debug(" Applying speculative solution techniques (guess and check)")

        S = speculator(self)
        S.solve()
        
        return    



class spec_node(object):

    def __init__(self,base_grid):
        self.grid = sudoku_puzzle(base_grid.as_lines())
        self.spec_ndxs = base_grid.get_unset_cells()
        self.child_base = {}

    def speculate(self,ndx,n):
        # Possible to speculate on this node at all?
        if ndx not in self.spec_ndxs():
            logging.debug(" Attempt to speculate on non-speculatable cell, ignoring.")
            return

        # Is n a legal value?
        if n not in self.grid.possibles[ndx]:
            logging.debug(" Value %d not allowed for cell %d,%d"%(n,ndx[0],ndx[1]))
            return

        # Have we already done this?
        if ndx not in self.child_base:
            self.child_base[ndx] = {}
        if n in self.child_base[ndx]:
            logging.debug(" Already speculated on value of %d in cell %d,%d"%(n,ndx[0],ndx[1]))
            return
        
        # So there is really something to do...
        logging.debug(" Speculating: what if %d,%d was set to %d?"%(ndx[0],ndx[1],n))
        new_node = spec_node(self.grid)
        new_node.grid.set_value(ndx,n)
        new_node.grid.solve()
        self.child_base[ndx][n] = new_node

    def has_solution(self):
        return self.grid.is_solved()
    
class speculator(object):

    def __init__(self,base_grid):
        self.base_grid = base_grid
        self.spec_tree = spec_node(base_grid)
        
    def solve(self):
        logging.debug("No here yet!")
    
    
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
    
