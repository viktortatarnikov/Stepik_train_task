from random import choice
with open('first_names.txt', 'r', encoding='utf-8') as ferst, open('last_names.txt', 'r', encoding='utf-8') as last:
    names1 = list(map(str.strip, ferst.readlines()))
    names2 = list(map(str.strip, last.readlines()))
    for _ in range(3):
        print(choice(names1), choice(names2))
