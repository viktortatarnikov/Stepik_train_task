from fractions import *
from  math import*
n = set()
num = int(input())
for i in range(1, num+1):
    for j in range(1, num+1):
        if Fraction(i, j) < 1:
            n.add(Fraction(i, j))
for ind in sorted(n):
    print(ind)
