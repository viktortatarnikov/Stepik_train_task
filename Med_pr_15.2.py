def sq_sum(*ar):
    res = [ind**2 for ind in ar]
    return sum(res)
print(sq_sum(1, 2, 3))