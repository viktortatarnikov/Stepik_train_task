def print_products(*ar):
    res = [ind for ind in ar if type(ind) == str and ind != '']
    if len(res) != 0:
        for ind in range(len(res)):
            print(str(ind + 1) + ')', res[ind])
    else:
        print('Нет продуктов')

print_products()
print_products('Тимур', 'Dfkthf', 'Саша')
print_products([4], {}, 1, 2, {'Beegeek'}, '')
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)