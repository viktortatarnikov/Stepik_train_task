high_ord_func = lambda x, func: x + func(x)

result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)

print(result)