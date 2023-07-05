with open('population.txt', 'r', encoding='utf-8') as countrys:
    names1 = list(map(str.strip, countrys.readlines()))
    for ind in names1:
        if ind[0] == 'G':
            if int(ind.split('\t')[1]) > 500000:
                print(ind.split('\t')[0])

