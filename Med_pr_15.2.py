def mean(*ar):
    res = [ind for ind in ar if type(ind) == int or type(ind) == float]
    if len(res) != 0:
        return sum(res)/len(res)
    else:
        return 0
print(mean(0))