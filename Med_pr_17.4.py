from decimal import *
with open('goats.txt', 'r', encoding='utf-8') as inpt, open('answer.txt', 'w', encoding='utf-8') as outp:
    colors = list(set(filter(lambda x: ' goat' in x, map(str.strip, inpt.readlines()))))

    inpt.seek(0)
    al = list(map(str.strip, inpt.readlines()))

    goat_dict = {key: 0 for key in colors}

    for ind in range(al.index('GOATS') + 1, len(al)):
        goat_dict[al[ind]] = goat_dict.get(al[ind], 0) + 1
    for key, value in sorted(goat_dict.items()):
        if Decimal(value/(len(al) - al.index('GOATS'))) >= Decimal(7/100):
            print(key, file=outp)
