from fractions import Fraction
n = int(input())
s = 0
for i in range(n):
    s += Fraction(1, (i + 1)**2)
print(s)
