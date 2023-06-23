from fractions import *
from  math import*
n = int(input())

lst = [Fraction(i, n-i) for i in range(n) if Fraction(i, n-i) < 1 and Fraction(i, n-i).numerator + Fraction(i, n-i).denominator == n]

print(max(lst))