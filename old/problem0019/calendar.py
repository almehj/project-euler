#!/usr/bin/env python3

days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
std_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def n_days(m,y):
    answer = 0
    if m == 1:
        if (y%100 == 0 and y%400 == 0) or (y%4 == 0 and y%100 != 0):
            answer = 1

    return answer+std_days[m]
            


date = 1
y = 1900
n = 0
while y <= 2000:
    y_n = 0
    for m in range(12):
#        print("  Year %d, Month %02d: %s"%(y,m+1,days[date]))
        date += n_days(m,y)
        date %= 7
        if date == 0:
            y_n += 1
    if y > 1900:
        n += y_n
    print("Year %d: %d"%(y,y_n))
    y += 1

print("Total first day Sundays: %d"%(n))

