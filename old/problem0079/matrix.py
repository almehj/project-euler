#!/usr/bin/env python

reln = []

with open("p079_keylog.txt") as infile:

    used = []
    for line in infile:
        digits = [int(n) for n in line.strip()]
        for d in digits:
            if d not in used:
                used.append(d)

        for i in 0,1:
            for j in range(i+1,3):
                f = (digits[i],digits[j])
                if f not in reln:
                    reln.append(f)



    used.sort()
    pr_used = [str(n) for n in used]
    combo = []
    print(" ".join([" "]+pr_used))
    for i in used:
        line = []
        n = 0
        for j in used:
            if (i,j) in reln:
                line.append('*')
                n += 1
            else:
                line.append(" ")

        combo.append((n,i))
        print(i," ".join(line + [str(n)]))

    combo.sort()
    combo.reverse()
    combo = [str(t[1]) for t in combo]
    print("".join(combo))
