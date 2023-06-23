from fractions import Fraction
a = input()
b = input()
print(a, '+', b, '=', Fraction(a) + Fraction(b))
print(a, '-', b, '=', Fraction(a) - Fraction(b))
print(a, '*', b, '=', Fraction(a) * Fraction(b))
print(a, '/', b, '=', Fraction(a) / Fraction(b))