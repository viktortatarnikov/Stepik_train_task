def pretty_print(data, side='-', delimiter='|'):
    data = [str(ind) for ind in data]
    res = delimiter
    for word in data:
        res += ' ' + word + " " + delimiter
    side1 = ' ' + ''.join([side for _ in range(len(res) - 2)]) + ' '
    print(side1)
    print(res)
    print(side1)


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')