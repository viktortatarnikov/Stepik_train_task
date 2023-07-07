with open('ledger.txt', 'r', encoding='utf-8') as file:
    a = file.readlines()

    print('$' + str(sum(map(lambda x: int(x.strip().lstrip('$')), a))))