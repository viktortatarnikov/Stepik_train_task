def greet(name, *ar):
    res = [ind for ind in ar]
    words = 'Hello, ' + name
    if len(res) != 0:
        words += ' and ' + ' and '.join(res)
        return words + '!'
    else:
        return words + '!'
print(greet('Тимур'))
print(greet('Тимур', 'Dfkthf', 'Саша'))