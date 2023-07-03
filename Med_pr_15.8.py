from functools import reduce
lst = [int(ind) for ind in input().split()]
x = int(input())

def evaluate(coefficients, x):
    index = list(range(len(coefficients)))[::-1]

    return reduce(lambda x, y: x + y, map(lambda a, index: a*(x**index), coefficients, index), 0)


print(evaluate(lst, x))