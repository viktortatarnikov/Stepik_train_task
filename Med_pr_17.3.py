def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as data:
        data_dikt = []
        keys = data.readline().strip().split(',')
        for value in data.readlines():
            items = value.strip().split(',')
            data_dikt.append(dict(zip(keys, items)))
    return data_dikt


for ind in read_csv():
    print(*ind.items())