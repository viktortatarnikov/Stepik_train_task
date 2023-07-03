def concat(*arg, sep=' '):
    new_arg = [str(word) for word in arg]
    res = sep.join(new_arg)

    return res


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

# Красивое решение
# def concat(*args, sep=' '):
#     return sep.join(map(str, args))