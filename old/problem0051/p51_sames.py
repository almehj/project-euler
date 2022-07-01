#!/usr/bin/env python

import sys

def get_primes(l):
    infile_name = "primes_len%02d.txt"%l

    with open(infile_name) as infile:
        return [line.strip() for line in infile]


done_commons = {}

def get_commons(locs,digit_map):

    answer = []

    prev_locs = tuple(locs[:-1])
    if prev_locs in done_commons:
        base = done_commons[prev_locs]
        magic_i = prev_locs[0]
        new_i = locs[-1]
        for n in base:
            if n[magic_i] == n[new_i]:
                answer.append(n)

    else:
        for d in "0123456789":
            keys = [(i,d) for i in locs]
            curr_common = digit_map.get(keys[0],[])
            for k in keys[1:]:
                new_common = []
                k_list = digit_map.get(k,[])
                for n in curr_common:
                    if n in k_list:
                        new_common.append(n)

                curr_common = new_common
                if len(curr_common) < 1:
                    break

            answer += curr_common

            
    done_commons[locs] = answer    
    return answer

def match_except(n,m,locs):

    for i,(c1,c2) in enumerate(zip(n,m)):
        if i not in locs:
            if c1 != c2:
                return False
    return True

def gather_lists(l,locs):

    used = {}
    answer = []
    
    for i,n in enumerate(l):
        if n in used:
            continue
        curr_set = [n]
        used[n] = 1
        for m in l[i+1:]:
            if m in used:
                continue
            if match_except(n,m,locs):
                curr_set.append(m)
                used[m] = 1
        answer.append(curr_set)

    return answer

def bin_rep(n):
    if n == 0:
        return '0'

    answer = []
    while n > 0:
        answer.append(str(n%2))
        n //= 2
        
    answer.reverse()    
    return ''.join(answer)

def locs_rep(n):
    answer = []

    i = 0
    while n > 0:
        if n%2 == 1:
            answer.append(i)
        n //= 2
        i += 1
    
    return tuple(answer)


def gen_locs_list(l_max):
    n_max = 2**l_max 

    answer = [locs_rep(n) for n in range(1,n_max)]
    answer = [(len(l),l) for l in answer]
    answer.sort()


    return [t[1] for t in answer]

def main():

    l_max = int(sys.argv[1])
    s_min = int(sys.argv[2])
    min_locs_len = 1
    if l_max > 2:
        min_locs_len = 2
        
    sys.stderr.write("reading...")
    sys.stderr.flush()    
    primes = get_primes(l_max)
    sys.stderr.write("done\n")
    
    sys.stderr.write("hashing...")
    sys.stderr.flush()    
    prime_d = {}    
    for n in primes:
        prime_d[n] = 1
    sys.stderr.write("done\n")

    sys.stderr.write("mapping...")
    sys.stderr.flush()    
    digit_map = {}
    for n in primes:
        for t in enumerate(n):
            if t not in digit_map:
                digit_map[t] = []
            digit_map[t].append(n)
    sys.stderr.write("done\n")

    locs_l = gen_locs_list(l_max)

    l_len = 1000000
    for locs in locs_l:
        if len(locs) < l_len:
            l_len = len(locs)
        if len(locs) < min_locs_len:
            continue

        sys.stdout.write("  getting commons for %s..."%(str(locs)))
        sys.stdout.flush()
        l = get_commons(locs,digit_map)
        print("done")
        
        sys.stdout.write("  gathering lists...")
        sys.stdout.flush()
        l2 = gather_lists(l,locs)
        print("done")
        
        for ls in l2:
            if len(ls) >= s_min:
                print(ls)
        
    
if __name__ == "__main__":
    main()
